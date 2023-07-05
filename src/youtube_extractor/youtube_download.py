from __future__ import unicode_literals
import youtube_dl
import sys, os, logging
import urllib.request
import urllib.parse
import re
import yt_dlp
import json
from bson import ObjectId
from datetime import datetime, timedelta
from inspect import currentframe, getframeinfo


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'services'))
from logger_track import events_logger

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'services/collections/crud_operations')))
from query_operations import add_one, update_ref_ids, aggregate_lookup_find_subcategory_name

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'services/create_directory')))
from create_folder import create_folder

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'services/util')))
from term_color import bcolors

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'schema/documents')))
from collections_doc import Video, Article, Topic


DATABASE_NAME = 'convertxt'

def insert_document_in_collection(db_name: str, coll_name: str, doc) -> str:
    new_doc_id = add_one( db_name, coll_name, doc )
    return new_doc_id.inserted_id

def build_document_collection(video_meta_info: dict) -> str:

    video_class_obj = Video(video_meta_info)
    video_doc = video_class_obj.video()
    video_inserted_id = insert_document_in_collection( DATABASE_NAME, 'video', video_doc) # Create a new video_doc to store thir info and ref id of ather coll


    article_obj = Article(video_inserted_id, video_meta_info)
    article_doc = article_obj.article_schema()
    article_inserted_id = insert_document_in_collection( DATABASE_NAME, 'article', article_doc) # Create a new topic to store thir info and ref id of ather coll
    

    topic_obj = Topic(video_inserted_id, article_inserted_id, video_meta_info)
    topic_doc = topic_obj.topic_schema()
    new_topic_id = insert_document_in_collection( DATABASE_NAME, 'topic', topic_doc)
    
    return new_topic_id

def ydl_progress_download_status(d):
    if d['status'] == 'finished':
        print(f"{bcolors.OKBLUE}\nDone downloading, now converting ... {bcolors.ENDC}")


def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < 60:
        return 'The video is too short'

class Ydl_Logger(object):
    def debug(self, msg):
       
        if msg.startswith('[debug] '):
            print(f"{bcolors.INFO_GREEN_BG} Ydl_Logger debug: {msg} {bcolors.ENDC}")
            pass
        else:
            self.info(msg)
        pass

    def info(self, msg):
        print(f"{bcolors.INFO_GREEN_BG} Ydl_Logger info: {msg} {bcolors.ENDC}")
        pass

    def warning(self, msg):
        frameinfo = getframeinfo(currentframe())
        events_logger(__name__, f" Ydl_Logger warning, line no {frameinfo.lineno}: {msg}", logging.WARN, logging.DEBUG)
        pass

    def error(self, msg):
        frameinfo = getframeinfo(currentframe())
        events_logger(__name__, f" Ydl_Logger error, line no {frameinfo.lineno}: {msg}", logging.ERROR, logging.DEBUG)
       
# Download youtube video by URL query 

def extract_audio_from_youtube_video(url: str, video_id: str, audio_storage_path: str) -> str:    
    # ydl_opts = {
    #     'match_filter': youtube_dl.utils.match_filter_func("!is_live"), 
    #     'retries':4, 
    #     'ignoreerrors': True, 
    #     'format': 'mp4', 
    #     'subtitleslangs': ['en'], 
    #     'writeautomaticsub': True, 
    #     'convertsubtitles': 'srt', 
    #     'restrictfilenames': True, 
    #     'outtmpl': fileDirectory
    # }
    ydl_opts = {
        'cachedir': False, # https://ostechnix.com/fix-unable-to-download-video-data-http-error-403-forbidden-error/
        'writesubtitles': True,
        'skip-download': True,
        'outtmpl': f''+ audio_storage_path + '/' + video_id,
        'noplaylist': True,
        'match_filter': youtube_dl.utils.match_filter_func("!is_live"), # https://stackoverflow.com/questions/68818306/youtubedl-in-script-completely-ignores-is-live-parameter
        # 'match_filter': longer_than_a_minute,
        'continue_dl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # 'mp3',
            'preferredquality': '192',
        }],
        'logger': Ydl_Logger(),
        'progress_hooks': [ydl_progress_download_status],
    }
    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ydl.cache.remove()
            video_meta_info = ydl.extract_info(url, download=False)
            ydl.prepare_filename(video_meta_info)
            ydl.download([url])
            
            topic_inserted_id = build_document_collection(video_meta_info) # Create a new topic to store thir info and ref id of ather coll
            
            print('insert_document_in_collection:', topic_inserted_id)
            return topic_inserted_id
    except:
        events_logger(__name__, f"Could not download the video in course: {url}", logging.ERROR, logging.DEBUG)
        

#  Searching and Get YouTube ID from URL

def search_youtube_id_from_url():
    pipeline = [{'$lookup': {'from': 'subcategory',
                            'localField': 'subcategory_ref_ids',
                            'foreignField': '_id',
                            'as': 'lookup_subcategory'
                            }
                }]

    aggregate_res = aggregate_lookup_find_subcategory_name("convertxt", "category", pipeline)
    
    for doc in aggregate_res:
        #    print("subcategories _ids:",doc)
        for subcat_id in doc['subcategory_ref_ids']:
            #    print('subcat_id:', doc)
            for sub_doc in doc['lookup_subcategory']:
                if subcat_id == sub_doc['_id']:
                    # print(f"Category name: '{doc['title']}', Subcategory name: '{sub_doc['title']}' _id: '{sub_doc['_id']}' ")
                    audio_storage_path = create_folder(doc['title'], sub_doc['title'])
                    print('audio_storage_path:', audio_storage_path)
                    # extract_audio_from_youtube_video("https://www.youtube.com/watch?v=dxGLaYdVizs", 'dxGLaYdVizs', audio_storage_path)

                    try:
                        subcategory_query_parameter = urllib.parse.urlencode({"search_query" : sub_doc['title']}) 
                        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + subcategory_query_parameter)
                        search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())
                        # print('Result length:',len(search_results_array),'\nResult of a search term that provaided :', search_results_array)
                        
                        # get YouTube video IDs from URL as array
                        for index, video_id in enumerate(search_results_array):
                            ref_ids = extract_audio_from_youtube_video("https://www.youtube.com/watch?v=" + video_id, video_id, audio_storage_path)
                            # update_ref_ids("convertxt", "subcategory", '6475ce5ef4cbf502a1205da9',ref_ids , [])
                            update_ref_ids("convertxt", "subcategory", sub_doc['_id'],ref_ids , [])
                            # if index == search_limit:
                            #     break
                            
                    except urllib.error.URLError as e:
                        print(f"Couldn't open {subcategory_query_parameter} Error: {e}")
                        events_logger(__name__, f"Couldn't open {subcategory_query_parameter} Error: {e}", logging.ERROR, logging.DEBUG)
                else:
                    print('ERROR::')
                    #    print(f"ERROR, DATA NOT MATCH: Category name: '{doc['name']}', Subcategory name: '{sub_doc['name']}', _id: '{sub_doc['_id']}'")
    


    # audio_storage_path = create_folder('doc', 'sub_doc')
    # https://www.youtube.com/watch?v=8MmMm2-kJV8

    # ref_ids = extract_audio_from_youtube_video("https://www.youtube.com/watch?v=" + 'tWPm0Q4fwY8', 'tWPm0Q4fwY8', audio_storage_path)
    # update_ref_ids("convertxt", "subcategory", '6475ce5ef4cbf502a1205da9',ref_ids , [])

    # extract_audio_from_youtube_video("https://www.youtube.com/watch?v=" + '79Dij1111/=@11ItQXMM', '79Dij1111/=@11ItQXMM', audio_storage_path)


    # print("Please, enter a search term:")
    # subcategory_query_parameter = urllib.parse.urlencode({"search_query" : input()})
    # print('subcategory_query_parameter:', subcategory_query_parameter)
    # html_content = urllib.request.urlopen("http://www.youtube.com/results?" + subcategory_query_parameter)
    # print('html_content:', html_content)
    # search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())

    # print('Result length:',len(search_results_array),'\nResult of a search term that provaided :', search_results_array)

    # # get YouTube video ID from URL
    # for i, video_id in search_results_array:
    #     print("******** https://www.youtube.com/watch?v=" + video_id, i)
    #     # extract_audio_from_youtube_video("https://www.youtube.com/watch?v=" + video_id, video_id)

from __future__ import unicode_literals
import youtube_dl
import sys
import urllib.request
import urllib.parse
import re
import yt_dlp
import json
import pprint
from bson import ObjectId
from datetime import datetime, timedelta
sys.path.append('/Users/eli/git_repos/python-projects/extract-audio-from-youtube-video/src/services/collections/crud_operations')
from query_operations import add_one, aggregate_lookup_find_subcategory_name


"""
def get_info():
    global video,lc,im5
    link_vid = txt2.get()
    try:
        video = pafy.new(link_vid)
    except Exception as e:
        error = tk.Label(windo, text="Something went wrong!! Please check URL", width=35, height=2, fg="white", bg="red",
                        font=('times', 18, ' bold '))
        error.place(x=274, y=370)
        windo.after(5000, destroy_widget, error)
        print(e)
def download_video_thumbnail():
    try:
        vid_id = video.videoid
        im5.save(vid_id+'.jpg')
        msg = tk.Label(windo, text='Thumbnail Downloaded', width=25, height=2, fg="white", bg="midnightblue",
                        font=('times', 18, ' bold '))
        msg.place(x=274, y=370)
        windo.after(5000, destroy_widget, msg)
    except Exception as e:
        print(e)
"""


def extract_meta_info_from_youtube_video(ydl, url):
    meta_info = ydl.extract_info(url, download=False)

    video_url = meta_info.get("url", None)
    video_id = meta_info.get("id", None)
    video_title = meta_info.get('title', None)
    # pprint.pprint(ydl.sanitize_info(meta_info))
    print('===============')
    # print('video_id: %s' % (video_id))
    # print('video_title: %s' % (video_title))
    # print('upload date : %s' % (meta_info['upload_date']))
    # print('uploader    : %s' % (meta_info['uploader']))
    # print('views       : %d' % (meta_info['view_count']))
    # print('likes       : %d' % (meta_info['like_count']))
    # print('comment_count       : %d' % (meta_info['comment_count']))
    # print('id          : %s' % (meta_info['id']))
    # print('format      : %s' % (meta_info['format']))
    # print('duration    : %s' % (meta_info['duration']))
    # print('title       : %s' % (meta_info['title']))
    # print('description : %s' % (meta_info['description']))
    # print('any       :', meta_info['requested_subtitles'])

    audio_info = {
        'video_id': video_id,
        'video_title': video_title,
        'upload_date': meta_info['upload_date'],
        'uploader': meta_info['uploader'],
        'views': meta_info['view_count'],
        'likes': meta_info['like_count'],
        'comment_count': meta_info['comment_count'],
        'id': meta_info['id'],
        'format': meta_info['format'],
        'duration': meta_info['duration'],
        'title': meta_info['title'],
        'description': meta_info['description'],
    }
    
    topic = {
            'title': audio_info['video_title'],
            'description': 'This is a Topic description filed',
            'video': {
                "url": video_url
            },
            "article": [ObjectId('645c9c8406fbde8ed928e002'), ObjectId('645c9c8406fbde8ed928e002'), ObjectId('645c9c8406fbde8ed928e002')],
            "author": "Author name",
            "views": audio_info['views'],
            "rating": 1.05,
            "subscribers": 12,
            "tags": ['#Topic1', '#Mobile.', '#Embedded.', '#Systems.','123'],
            "created_at": datetime.today(),
            "updated_at": datetime.today() 
        }

    add_one('convertxt', 'topic', topic)

def progress_download_status(d):
    if d['status'] == 'finished':
        print('\nDone downloading, now converting ...')

# Download youtube video by URL query 

def extract_audio_from_youtube(url, video_id):    
    folder_name = 'converted_audio'
    file_name = video_id
    ydl_opts = {
        'writesubtitles': True,
        'skip-download': True,
        'outtmpl': f'/Users/eli/git_repos/python-projects/extract-audio-from-youtube-video/'+folder_name+'/' + file_name,
        'noplaylist': True,
        'continue_dl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [progress_download_status],
    }
    try:
        url = 'https://www.youtube.com/watch?v='+video_id
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        extract_meta_info_from_youtube_video(ydl, url)
        
    except Exception:
        return False

#  Extract YouTube ID from URL
# Searching youtube videos by a string user input / Get YouTube ID from URL 
def search_youtube_id_from_url():
    pipeline = [{'$lookup': {'from': 'subcategories',
                            'localField': 'subcategories',
                            'foreignField': '_id',
                            'as': 'lookup_subcategories1'
                            }
                }]

    aggregate_res = aggregate_lookup_find_subcategory_name("contxt", "categories", pipeline)

    # for doc in aggregate_res:
    #     #    print("subcategories _ids:",doc)
    #     for subcat_id in doc['subcategories']:
    #         #    print('subcat_id:', doc)
    #         for sub_doc in doc['lookup_subcategories1']:
    #             if subcat_id == sub_doc['_id']:
    #                 #    if _ids match call youtube procsess by Subcategory name
    #                 print(f"Category name: '{doc['name']}', Subcategory name: '{sub_doc['name']}' _id: '{sub_doc['_id']}' ")
    #             else:
    #                 print('ERROR::')
    #                 #    print(f"ERROR, DATA NOT MATCH: Category name: '{doc['name']}', Subcategory name: '{sub_doc['name']}', _id: '{sub_doc['_id']}'")
        

    # topics_of_subcat = {
    #     '111111111': ['F_QFkE-UbGM', 'dxGLaYdVizs'],
    #     '222222222': ['79DijItQXMM', 'WX8HmogNyCY'],
    #     '333333333': ['fN1Cyr0ZK9M', 'aWKtAqIUEl4'],
    #     'AAAAAAAAAAA': ['-RNG_tTXXcg', '7C7u5Kud1Y0'],
    #     'BBBBBBBBBBB': ['klDHM_sxYxs', '1edHjgZnnaw'],
    #     'CCCCCCCCCCC': ['XKGq0hAUMRo', 'RXRWE_XQ8aE'],
    #     'aaaaaa': ['kQDw88hEr2c', 'A0azOIk0Kvg'],
    #     'bbbbbb': ['KP_XkN2v7OM', 'yg8116aeD7E'],
    #     'cccccc': ['hAYUQ1ltJj0', 'NvR9YOpDG4A'],
    # }
    # for subcategory, topics in topics_of_subcat.items():
    #     for i, video_id in enumerate(topics):
    #         print('video_id:', i, video_id)
    #         extract_audio_from_youtube("https://www.youtube.com/watch?v=" + video_id, video_id)


    # extract_audio_from_youtube("https://www.youtube.com/watch?v=" + 'WX8HmogNyCY', 'WX8HmogNyCY')

    print("Please, enter a search term:")

    subcategory_query_parameter = urllib.parse.urlencode({"search_query" : input()})
    print('subcategory_query_parameter:', subcategory_query_parameter)
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + subcategory_query_parameter)
    print('html_content:', html_content)
    search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())

    print('Result length:',len(search_results_array),'\nResult of a search term that provaided :', search_results_array)

    # get YouTube video ID from URL
    for i, video_id in enumerate(search_results_array):
        print(" YouTube video ID + URL: https://www.youtube.com/watch?v=" + video_id, i)
        # extract_audio_from_youtube("https://www.youtube.com/watch?v=" + video_id, video_id)

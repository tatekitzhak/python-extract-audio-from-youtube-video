from __future__ import unicode_literals
import yt_dlp

folder_name = 'converted_video_download'
audio_file_name1 = 'F_QFkE-UbGM'
audio_file_long = '8hly31xKli0'
audio_file_short = 'BaW_jenozKc'

ydl_opts = {
    'writesubtitles': True, 
    'skip-download': True,
         'outtmpl': f'/Users/eli/git_repos/python-projects/extract-audio-from-youtube-video/'+folder_name+'/'+audio_file_name1,
         'noplaylist': True,
         'continue_dl': True,
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'wav',
             'preferredquality': '192',
             }]
     }

url ='https://www.youtube.com/watch?v='+audio_file_name1
# url = 'https://www.youtube.com/watch?v=' + audio_file_short
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
info_dict = ydl.extract_info(url, download=False)
video_url = info_dict.get("url", None)
video_id = info_dict.get("id", None)
video_title = info_dict.get('title', None)

print('info_dict : %s' %(info_dict))
print('video_id: %s' %(video_id))
print('video_title: %s' %(video_title))


meta = ydl.extract_info(url, download=False)

print ('upload date : %s' %(info_dict['upload_date']))
print ('uploader    : %s' %(info_dict['uploader']))
print ('views       : %d' %(info_dict['view_count']))
print ('likes       : %d' %(info_dict['like_count']))
# print ('dislikes    : %d' %(info_dict['dislike_count']))
print ('id          : %s' %(info_dict['id']))
print ('format      : %s' %(info_dict['format']))
print ('duration    : %s' %(info_dict['duration']))
print ('title       : %s' %(info_dict['title']))
print ('description : %s' %(info_dict['description']))



############### Searching youtube videos by a string user input ##########

# import urllib.request
# import urllib.parse
# import re

# print("Please, enter search query:")

# query_string = urllib.parse.urlencode({"search_query" : input()})
# html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
# search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())
#          #  https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb

# print('Search query that provaided : %s' %(search_results_array))
# for i in search_results_array:
#    print("https://www.youtube.com/watch?v=" + i)


# if __name__ == '__main__':


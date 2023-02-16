

#######  https://stackoverflow.com/questions/40713268/download-youtube-video-using-python-to-a-certain-directory
#######  https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL
#######  https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
#######  https://www.codegrepper.com/code-examples/python/youtube-dl+python+download+to+specific+folder
#######  https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
####### https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL
####### https://github.com/ytdl-org/youtube-dl/blob/master/README.md#format-selection
####### https://www.programcreek.com/python/?code=DuckBoss%2FJJMumbleBot%2FJJMumbleBot-master%2FJJMumbleBot%2Fplugins%2Fextensions%2Fsound_board%2Futility%2Fsound_board_utility.py


############### Download youtube video by URL query ##########

from __future__ import unicode_literals
import youtube_dl

folder_name = 'converted_video_download'
audio_file_name = 'F_QFkE-UbGM'

ydl_opts ={
         'outtmpl': f'/Users/eli/git_repos/python-script-extract-yt-video-data/'+folder_name+'/'+audio_file_name,
         'noplaylist': True,
         'continue_dl': True,
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'wav',
             'preferredquality': '192',
             }]
     }

url ='https://www.youtube.com/watch?v='+audio_file_name
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
# info_dict = ydl.extract_info(url, download=False)
# video_url = info_dict.get("url", None)
# video_id = info_dict.get("id", None)
# video_title = info_dict.get('title', None)

# print('info_dict : %s' %(info_dict))
# print('video_id: %s' %(video_id))
# print('video_title: %s' %(video_title))


# meta = ydl.extract_info(url, download=False)

# print ('upload date : %s' %(info_dict['upload_date']))
# print ('uploader    : %s' %(info_dict['uploader']))
# print ('views       : %d' %(info_dict['view_count']))
# print ('likes       : %d' %(info_dict['like_count']))
# print ('dislikes    : %d' %(info_dict['dislike_count']))
# print ('id          : %s' %(info_dict['id']))
# print ('format      : %s' %(info_dict['format']))
# print ('duration    : %s' %(info_dict['duration']))
# print ('title       : %s' %(info_dict['title']))
# print ('description : %s' %(info_dict['description']))



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


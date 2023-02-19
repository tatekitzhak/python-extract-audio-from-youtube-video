#######  https://stackoverflow.com/questions/40713268/download-youtube-video-using-python-to-a-certain-directory
#######  https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL
#######  https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php
#######  https://www.codegrepper.com/code-examples/python/youtube-dl+python+download+to+specific+folder


############### Searching youtube videos by a string user input ##########

# import urllib.request
# import urllib.parse
# import re
#
# print("Please, enter search query:")
#
# query_string = urllib.parse.urlencode({"search_query" : input()})
# html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
# search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())
#          #  https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb
#
# print('Search query that provaided : %s' %(search_results_array))
# for i in search_results_array:
#    print("https://www.youtube.com/watch?v=" + i)

from __future__ import unicode_literals
import yt_dlp

folder_name = 'converted_video_download'
audio_file_name1 = 'F_QFkE-UbGM'
audio_file_long = '8hly31xKli0'


def my_hook(d):
    if d['status'] == 'finished':
        print('\nDone downloading, now converting ...')


ydl_opts = {
    'writesubtitles': True,
    'skip-download': True,
    'outtmpl': f'/Users/eli/git_repos/python-projects/extract-audio-from-youtube-video/'+folder_name+'/'+audio_file_name1,
    'noplaylist': True,
    'continue_dl': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',  # 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [my_hook],
}

url = 'https://www.youtube.com/watch?v='+audio_file_name1
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
meta = ydl.extract_info(url, download=False)
video_url = meta.get("url", None)
video_id = meta.get("id", None)
video_title = meta.get('title', None)

# print('meta : %s' % (meta))
print('video_id: %s' % (video_id))
print('video_title: %s' % (video_title))

print('upload date : %s' % (meta['upload_date']))
print('uploader    : %s' % (meta['uploader']))
print('views       : %d' % (meta['view_count']))
print('likes       : %d' % (meta['like_count']))
# print ('dislikes   : %d' % (meta['dislike_count']))
print('id          : %s' % (meta['id']))
print('format      : %s' % (meta['format']))
print('duration    : %s' % (meta['duration']))
print('title       : %s' % (meta['title']))
print('description : %s' % (meta['description']))

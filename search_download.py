from __future__ import unicode_literals
import youtube_dl

import urllib.request
import urllib.parse
import re

# Searching youtube videos by a string user input 
def search_youtube_video():
    print("Please, enter search query:")

    query_string = urllib.parse.urlencode({"search_query" : input()})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())

    print('Search query that provaided : %s' %(search_results_array))
    for i in search_results_array:
        print("******** https://www.youtube.com/watch?v=" + i)
        download_youtube_video("https://www.youtube.com/watch?v=" + i, i)

# Download youtube video by URL query 

def download_youtube_video(url, name):    
    folder_name = 'test'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'/Users/eli/git_repos/python-script-extract-yt-video-data/'+folder_name+'/'+name+'.wav',
        'noplaylist': True, 
        'continue_dl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192', }]
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=False)
            ydl.prepare_filename(info_dict)
            ydl.download([url])
    except Exception:
        return False

search_youtube_video()
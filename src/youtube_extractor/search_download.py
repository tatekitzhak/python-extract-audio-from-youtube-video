from __future__ import unicode_literals
import youtube_dl

import urllib.request
import urllib.parse
import re
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
# Searching youtube videos by a string user input 
def youtube_search():
    print("Please, enter a search term:")

    query_string = urllib.parse.urlencode({"search_query" : input()})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results_array = re.findall(r"watch\?v=(.{11})", html_content.read().decode())

    print('Search term that provaided : %s' %(search_results_array))
    for i in search_results_array:
        print("******** https://www.youtube.com/watch?v=" + i)
        extract_audio_from_youtube("https://www.youtube.com/watch?v=" + i, i)

# Download youtube video by URL query 

def extract_audio_from_youtube(url, name):    
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

youtube_search()
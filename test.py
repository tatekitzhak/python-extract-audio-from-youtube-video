from __future__ import unicode_literals
import youtube_dl

folder_name = 'test'
audio_file_name = '8hly31xKli0'

def download_clip(url, name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'/Users/eli/git_repos/python-script-extract-yt-video-data/'+folder_name+'/'+name+'.wav',
        'noplaylist': False,
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
            return True
    except Exception:
        return False

url_path ='https://www.youtube.com/watch?v='+audio_file_name
download_clip(url_path, audio_file_name)
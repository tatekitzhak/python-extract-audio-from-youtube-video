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
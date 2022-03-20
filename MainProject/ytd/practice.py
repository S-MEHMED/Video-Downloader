# from pytube import YouTube
# # res='144p'
# # quality='48kbps'

# obj=YouTube('https://www.youtube.com/watch?v=TkYEN69cQf0')

# # # video = obj.streams.filter(progressive=True).asc()
# audio=obj.streams.filter(only_audio=True).asc()
# for i in audio:
#     a=i.filesize/1024
#     if a > 999:
#         a=a/1024
#         a=round(a,2)
#         print(f"{a} mb")
#     else:
#         a=round(a,2)
#         print(f" {a} kb")
# # print(video)
# print(audio)
# a=[]
# a=video
# a=list(a)+list(audio)

# for i in a:

#     print(i.abr+i.mime_type[5:])
#     print(i.resolution)
#     if i.abr == quality:
#         video.get_by_itag(i.itag).download('/download')
# print('done')
# # tag='17'
# # a=video.get_by_itag(tag).download('/download')


# # video.download('/download')
# # vidoe=video

# for i in a:
#     if i.resolution == res:
#         video.get_by_itag(i.itag).download('/download')
#         print('done')


# from pytube import YouTube
# import os
# import subprocess
# import time


# url = 'https://www.youtube.com/watch?v=TkYEN69cQf0'

#     # Title and Time
# print("...")
# print(((YouTube(url)).title))
# print("...")
# # "//", (int(var1)/60),"mins")
#     # Filename specification
#     # Prevents any errors during conversion due to illegal characters in name
# _filename = 'khan'

#     # Downloading
# print("Downloading....")
# obj=YouTube(url)
# audio=obj.streams.filter(only_audio=True)
# for i in audio:

#     print(i.abr+i.mime_type[5:])
#     print(i.resolution)
#     if i.abr == '128kbps':
#         audio.get_by_itag(i.itag).download('.download/',filename=_filename)

#         time.sleep(1)

#     # Converting
# mp4 = "'%s'.mp4" % _filename
# mp3 = "'%s'.mp3" % _filename
# ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
# subprocess.call(ffmpeg, shell=True)

#     # Completion
# print("\nCOMPLETE\n")


# from pytube import YouTube
# import os
# import subprocess
# import time

# url = "https://www.youtube.com/watch?v=TkYEN69cQf0"
# var1=YouTube(url).length
#     # Title and Time
# print("...")
# print(((YouTube(url)).title), "//", (int(var1)/60),"mins")
# print("...")

#     # Filename specification
#     # Prevents any errors during conversion due to illegal characters in name
# _filename = 'sultan'

#     # Downloading
# print("Downloading....")
# a=YouTube(url).streams.first().download("",filename=_filename)
# time.sleep(1)

#     # Converting
# # mp4 = "'%s'.mp4" % _filename
# # mp3 = "'%s'.mp3" % _filename
# # ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
# # subprocess.call(ffmpeg, shell=True)
# base, ext = os.path.splitext(a)
# new_file= base + '.mp3'
# os.rename(a,new_file)

#     # Completion
# print("\nCOMPLETE\n")
# from pytube import YouTube
# url=YouTube('https://www.youtube.com/watch?v=TkYEN69cQf0')
# result_audio= url.streams.filter(only_audio=True).asc()
# for i in result_audio:
#     print(i)


# import requests
# import re
# from bs4 import BeautifulSoup
# chunk_size=256
# url="https://web.facebook.com/islamicnasheed4all/videos/310132296968000"
# r = requests.get(url,allow_redirects=True)
# # open('facebook.png', 'wb').write(r.content)

from pytube import YouTube
url = "https://www.youtube.com/watch?v=TkYEN69cQf0"
obj = YouTube(url)


# video = obj.streams.filter(progressive=True).asc()


# video = list(dict.fromkeys(video))
# # for i in video:
# #     print(i.resolution)
# print(type(video))
filesize = []
b = 1111000

if int(b) > 999999:
    c = f'{round(int(b) / 1000000,2)}gb'
    filesize.append(c)
elif int(b) > 999:
    c = f'{round(int(b)/1000,2)}mb'
    filesize.append(c)
else:
    c = f'{round(int(b),2)}kb'
    filesize.append(c)
print(filesize)

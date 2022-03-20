from __future__ import unicode_literals
from django.shortcuts import redirect
from django.shortcuts import render
# from django.urls import 
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .form import formdata
from .models import Todo
import os
import re
import yt_dlp
import youtube_dl
import sys
from collections import OrderedDict
import itertools

        # Area for Global variables
audio_id =''
url = ''
title = ''
thumbnail = '#'
global webpage_urls
webpage_urls=[]





def home(request):
    return render(request, 'ytb_main.html ')


    
    
        
def playlist_download(request):
    i = request.POST.get('id_value')
    print(i)
    print('i am playlist_download function')
    
    global url
    global audio_id
    global title
    global thumbnail
    global webpage_urls

    duration=''
    format_ids =[]
    filesize =[]
    file_s=[]
    cod=[]
    resolution =[]
    extension =[]
    formats =[]
    vcodec=[]
    vbr=[]

    regex_youtube = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
    regex_vimeo = r'^(http(s)?:\/\/)?((w){3}.|(player.))?vimeo?(\.com)?\/.+'
    regex_bili = r'^(http(s)?:\/\/)?((w){3}.)?bilibili?(\.com)?\/.+'

    

    # print(i)
    # print("this is webpage url from playlist ",webpage_urls)
    i = int(i)
    url = webpage_urls[i]
    print(url)

    
               
    
    
    
    
    
    
    
    
    
    
   
    

    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)

    for k, v in meta.items():
        
        if k == "duration":
            try:

                duration = v
                if duration > 3600:
                    duration=round(duration/3600,2)
                    duration = str(duration)+'hr'
                    
                elif duration > 60:
                    duration = round(duration/60,2)
                    duration = str(duration)+'min'
                    

                else:
                    duration=str(duration)+'sec'
                   

            except:
                duration = 'NaN'
                

        elif k == 'duration_string':
            duration = v
            
            if len(duration) <=2:
                duration = duration+" sec"
            elif len(duration) <=5:
                duration = duration + " minutes"
            elif len(duration) > 5:
                duration = duration + " hours"
        elif k == 'title':
            title=v
            
        
        elif k == "thumbnail":
            thumbnail = v
                
            
        
        elif k == 'formats':
            for i in v:
                for a, b in i.items():
                    if a == 'format_id':
                        format_ids.append(b)
                    elif a == 'format':
                        formats.append(b)
                    elif a == 'resolution':
                        resolution.append(b)
                    elif a == 'ext':
                        extension.append(b)
                    elif a == 'filesize':
                        filesize.append(b)
                    elif a == 'acodec':
                        cod.append(b)
                    elif a == 'filesize_approx':
                        file_s.append(b)
                    elif a == 'tbr':
                        vbr.append((b))
                    elif a == 'vcodec':
                        vcodec.append((b))
        elif k == 'entries':
            print('This is entries condition')
            
                
            for i in v:
                for a, b in i.items():
                    

                    
                    if a == 'formats':
                        
                        for d in b:
                            for i,j in d.items():
                                if i == 'format_id':
                                    format_ids.append(j)
                                elif i == 'resolution':
                                    resolution.append(j)
                                elif i == 'acodec':
                                    cod.append(j)
                                elif i == 'filesize_approx':
                                    file_s.append(j)
                                elif i == 'ext':
                                    extension.append(j)
                                elif i == 'tbr':
                                    vbr.append(j)
                                elif i == 'vcodec':
                                    vcodec.append(j)
                        
                    elif a == 'thumbnail':
                        thumbnail = b
                    elif a == 'duration':
                        duration = b
                        if duration > 3600:
                            duration=round(duration/3600,2)
                            duration = str(duration)+'hr'
                            
                        elif duration > 60:
                            duration = round(duration/60,2)
                            duration = str(duration)+'min'
                            

                        else:
                            duration = round(duration,2)
                            duration=str(duration)+'sec'
                    
                                                    
                    elif a == 'format_id':
                        format_ids.append(b)
                    
                    elif a == 'resolution':
                        resolution.append(b)
                    elif a == 'ext':
                        extension.append(b)
                    elif a == 'filesize':
                        filesize.append(b)
                    elif a == 'acodec':
                        cod.append(b)
                    elif a == 'filesize_approx':
                        file_s.append(b)
                    elif a == 'tbr':
                        vbr.append((b))     
                    elif a == 'vcodec':
                        vcodec.append((b))   
        
    
    if re.match(regex_youtube, url):
        global audio_id
        print("Before processing audio id is = ",audio_id)
        
        value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
        
        size=0
        f=[]
        up=[]
        s =len(format_ids)-len(filesize)
        del resolution[0:s] 
        del extension[0:s] 
        del format_ids[0:s] 
    
        
    

        resolution.reverse()
        extension.reverse()
        format_ids.reverse()
        filesize.reverse()
        cod.reverse()
        vbr.reverse()

        value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
        for i,j in zip(resolution,extension):
            f.append(i+j)



    
        s=len(resolution)
        s1=len(extension)
        s2=len(format_ids)
        s3=len(filesize)
        s4=len(cod)
        s5= len(vbr)
        

    

        for i,j in enumerate(f):
            
            if j not in up:
                up.append(j)
            else:
                # print(i) 3,6,10,11,12
                resolution.pop(i-s)
                extension.pop(i-s1)
                format_ids.pop(i-s2)
                filesize.pop(i-s3)
                cod.pop(i-s4)
                vbr.pop(i-s5)
        
        
        
    
        num = filesize.count(None)
        file_s.reverse()
        c=0
    
        for i,j in enumerate(filesize):
        
            if j == None:
                filesize[i]=file_s[-(num-c)]
                c+=1

    
    
        
        value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
        audio_id = ''
        for i,r,s,e,c,t in value:
            if r == 'audio only' and e == 'm4a':
                audio_id = i
                size = int(s)
                print('This is audio size',size)
            

        print(audio_id)
        file_s=[]
        for s,c in zip(filesize,cod):
            if c != 'mp4a.40.2':
                s+=size
                file_s.append(s)
            else:
                file_s.append(s)
            
        val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr)
        
        return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
        
        
        
    
        
    elif re.match(regex_bili,url):
        
        val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,vcodec)
        
        size_=0
        audio_id=''
        i=[]
        r=[]
        e=[]
        s=[]
        v=[]
        for ids,res,ext,size,vb,vcd in val:
        #     print(ids,'',res,'',ext,'',size,'',vb,'',vcd)
            if ext == 'm4a' and vcd == 'none':
                if size not in s:
                    audio_id=ids
                    size_=size
                    i.append(ids)
                    r.append(res)
                    e.append(ext)
                    s.append(size)
                    v.append(vb)
            
            elif  vcd[:4] == 'avc1':
                print('this is first if condition')
                i.append(ids)
                r.append(res)
                e.append(ext)
                s.append(size+size_)
                v.append(vb)
            # elif vcd == 'none':
            #     print('this is second if condition')
                

                # i.append(ids)
                # r.append(res)
                # e.append(ext)
                # s.append(size)
                # v.append(vb)

        # print(i)
        # print(r)
        # print(e)
        # print(s)
        # print(v)
            
        print(audio_id)
        
        # print('i am at last point of bili')
        value = itertools.zip_longest(i,r,e,s,v)
        
        return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
        
                    
    elif re.match(regex_vimeo,url):

        format_ids.reverse()
        resolution.reverse()
        extension.reverse()
        vbr.reverse()
        cod.reverse()

        
        val = itertools.zip_longest(format_ids,extension,resolution,vbr,cod)
        i=[]
    
    
        e=[]
        r=[]
        t=[]
    
    
        for ids,ext,res,tb,co in val:
            # print(ids,'----',res,'----',ext,'----',tb,'----',co)
            #ids[:28]
            # print(res)
            # print(ids[:29])
            # print(co,ext)
            # print(ext)
        
        
            if  res == "audio only" and ext == 'm4a' and co != 'mp4a.40.2':
                if ids[:11] == 'dash-akfire':
                    i.append(ids)
                    e.append(ext)
                    r.append(res)
                    t.append(tb)

                
                # print(co)
            
                

                # i.append(ids)
            
                # t.append(tb)
                # e.append(ext)
                # r.append(res)
            if 'http' in ids or 'source' in ids:
                i.append(ids)
            
                t.append(tb)
                e.append(ext)
                r.append(res)

        
            
        print('vimeo')
        
        value = itertools.zip_longest(i,r,e,t)
        return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
        

def submit(request):
    print('I am submit function')
    global url
    


    if url is None:
        print("url is None")
    global audio_id
    audio_id=''
    global title
    global thumbnail
    global webpage_urls
    webpage_urls=[]
    duration = ''
    format_ids =[]
    filesize =[]
    file_s=[]
    cod=[]
    resolution =[]
    extension =[]
    formats =[]
    vcodec=[]
    vbr=[]
    titles=[]
    vid_ids=[]



    # if request.method == 'POST':
    #     url = request.POST.get('URL')
    #     # new = Todo(url=url)
    #     # new.save()
    # print(url)
    
    
    
    
    

                # ''' Regex to match url '''
    regex_youtube = r'^(http(s)?:\/\/)?((w){3}.|m.)?youtu(be|.be)?(\.com)?\/.+'
    # regex_youtube_playlist = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/(playlist)+'
    regex_twitter = r'^(http(s)?:\/\/)?((w){3}.)?twitter?(\.com)?\/.+'
    regex_khan_acdmy = r'^(http(s)?:\/\/)?((w){3}.)?khanacademy?(\.org|.com)?\/.+'
    regex_reddit = r'^(http(s)?:\/\/)?((w){3}.)?reddit?(\.org|.com)?\/.+'
    # veoh,khan_acedmy,reddit
    regex_vimeo = r'^(http(s)?:\/\/)?(((w){3}.)|(player.))?vimeo?(\.com)?\/.+'
    regex_VLive = r'^(http(s)?:\/\/)?((w){3}.)?vlive?(\.tv)?\/.+'
    regex_daily_motion = r'^(http(s)?:\/\/)?((w){3}.)?dailymotion?(\.com)?\/.+'
    regex_SoundCloud = r'^(http(s)?:\/\/)?((w){3}.)?soundcloud?(\.com)?\/.+'
    regex_instagram = r'^(http(s)?:\/\/)?((w){3}.)?instagram?(\.com)?\/.+'
    regex_fb = r'^(http(s)?:\/\/)?((w){3}|m|fb|web)?(.facebook|.watch)?(\.com)?\/.+'
    regex_puhutv = r'^(http(s)?:\/\/)?((w){3}.)?puhutv?(\.com)?\/.+'
    regex_streamable = r'^(http(s)?:\/\/)?((w){3}.)?streamable?(\.com)?\/.+'
    regex_vk = r'^(http(s)?:\/\/)?((w){3}.)?vk?(\.com)?\/.+'
    regex_tiktok = r'^(http(s)?:\/\/)?((w){3}.)?tiktok?(\.com)?\/.+'
    regex_espn = r'^(http(s)?:\/\/)?((w){3}.)?espn?(\.com)?\/.+'
    regex_cnn = r'^(http(s)?:\/\/)?((w){3}|edition)?(.cnn)?(\.com)?\/.+'
    regex_ok_ru = r'^(http(s)?:\/\/)?((w){3}.|ok.)?ru?(\/video)?\/.+'
    regex_ted = r'^(http(s)?:\/\/)?((w){3}.)?ted?(\.com)?\/.+'
    regex_bili = r'^(http(s)?:\/\/)?((w){3}.)?bilibili?(\.com)?\/.+'

    # if re.match(regex_fb,url):
    #     with youtube_dl.YoutubeDL() as ydl:
    #         meta = ydl.extract_info(url, download=False)
    #         for k, v in meta.items():
    #             if k == 'webpage_url':
    #                 url = v
    
    
    
    
    
    uploader_url = ''
    ids = []
    key=[]
    count = 1
    
    ydl_opts = {
        'playliststart':1,
        'playlistend':5,
        'cachedir': False,
    }
    
        
    url = request.POST.get('url')
    # url = 'https://youtu.be/TkYEN69cQf0'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)

    
        

    for k,v in meta.items():
        key.append(k)
        if k == 'playlist_count':
            count = v
    if ('_type' in key and  ("playlist_count" in key and count != 1)):
        # webpage_urls=[]

        print('Now i am in playlist processing')

        
        ydl_opts = {
                
                # 'playliststart':22,
                # 'playlistend':39

            }

        
            
            
        
        for i, j in meta.items():
            
            if i == 'entries':
                
                for a in j:
                    
                    for x, y in a.items():
                        
                        if x == 'title':
                            titles.append(y)
                        

                            
                            
                        elif x == 'webpage_url':
                            # vid_ids=[]
                            
                            webpage_urls.append(y)
                            
                            
                        

        
        # print('webpage url',webpage_urls)
        for i in range(len(webpage_urls)):
            vid_ids.append(i)
            # print(vid_ids)
        
        
        
        values= itertools.zip_longest(vid_ids,titles)
   

    

        return render(request, 'playlist.html',{"values":values})
    


    else:
        print('This is not a playlist')
        # ydl_opts = {}
        # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #     meta = ydl.extract_info(url, download=False)

        for k, v in meta.items():
            # print(k)
            
            
        
            if k == "duration":
                try:

                    duration = v
                    if duration > 3600:
                        duration=round(duration/3600,2)
                        duration = str(duration)+'hr'
                    elif duration > 60:
                        duration = round(duration/60,2)
                        duration = str(duration)+'min'
                    else:
                        duration=str(duration)+'sec'
                except:
                    duration = 'NaN'
            elif k == 'duration_string':
                duration = v
                if len(duration) <=2:
                    duration = duration+" sec"
                elif len(duration) <=5:
                    duration = duration + " minutes"
                elif len(duration) > 5:
                    duration = duration + " hours"
            elif k == 'title':
            
                title = v
            elif k == 'uploader_url':
                uploader_url=v
            elif k == "thumbnail" and v != 'NaN':
                
        
            
                thumbnail = v
            
            elif k == 'formats':
                print('formats')
                for i in v:
                    for a, b in i.items():
                        if a == 'format_id':
                            format_ids.append(b)
                        elif a == 'format':
                            formats.append(b)
                        elif a == 'resolution':
                            resolution.append(b)
                        elif a == 'ext':
                            extension.append(b)
                        elif a == 'filesize':
                            filesize.append(b)
                        elif a == 'acodec':
                            cod.append(b)
                        elif a == 'filesize_approx':
                            file_s.append(b)
                        elif a == 'tbr':
                            vbr.append((b))
                        elif a == 'uploader_url':
                            uploader_url = b
                        # elif a == 'tbr':
                        #     tbr.append((b))
                     
            elif k == 'entries':
                print("entries")
                
                for i in v:
                    for a, b in i.items():
                        

                        
                        if a == 'formats':
                            print('this is bilibili')
                            for d in b:
                                for i,j in d.items():
                                    if i == 'format_id':
                                        format_ids.append(j)
                                    elif i == 'resolution':
                                        resolution.append(j)
                                    elif i == 'acodec':
                                        cod.append(j)
                                    elif i == 'filesize_approx':
                                        file_s.append(j)
                                    elif i == 'ext':
                                        extension.append(j)
                                    elif i == 'tbr':
                                        vbr.append(j)
                                    elif i == 'vcodec':
                                        vcodec.append(j)
                                    elif a == 'uploader_url':
                                        uploader_url = b
                        elif a == 'webpage_url':
                            uploader_url = b 
                        elif a == 'thumbnail':
                            thumbnail = b
                        elif a == 'duration':
                            duration = b
                            if duration > 3600:
                                duration=round(duration/3600,2)
                                duration = str(duration)+'hr'
                                
                            elif duration > 60:
                                duration = round(duration/60,2)
                                duration = str(duration)+'min'
                                

                            else:
                                duration = round(duration,2)
                                duration=str(duration)+'sec'
                        
                                                        
                        
                        elif a == 'format_id':
                            format_ids.append(b)
                        
                        elif a == 'resolution':
                            print("This is resolution",b)
                            resolution.append(b)
                        elif a == 'ext':
                            extension.append(b)
                        elif a == 'filesize':
                            filesize.append(b)
                        elif a == 'acodec':
                            cod.append(b)
                        elif a == 'filesize_approx':
                            file_s.append(b)
                        elif a == 'tbr':
                            vbr.append((b))
                        
                        

        if re.match(regex_fb, url):
            
            index=[]
        

            for i,j in enumerate(format_ids):
                if 'sd' in j or 'hd' in j:
                    index.append(i)
            for i in index:
                file_s.insert(i,'NaN')
            i=[]
            r=[]
            s=[]
            e=[]
            t=[]

            val = itertools.zip_longest(format_ids,resolution,file_s,extension,vbr)

            for ids,res,size,ext,tbb in val:
            
            
            

                if  ids[-1] == '0' or ids == 'sd' or ids == 'hd'  :
                
                    i.append(ids)
                    r.append(res)
                    s.append(size)
                    e.append(ext)
                    t.append(tbb)
                    # value = zip(i,r,s,e,t)
                # for j,k,l,m,n in value:
                #     if m == 'm4a':
                #         audio_id= j
                # value = itertools.zip_longest(i,r,s,e,t)
            
                # return render(request, 'fb_dow.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})
        
                elif ids[-1] != '0' and ids[-1] != '1':

                    i.append(ids)
                    r.append(res)
                    s.append(size)
                    e.append(ext)
                    t.append(tbb)
            value = zip(i,r,s,e,t)
            audio_id=''
            size=0
            for j,k,l,m,n in value:
                if m == 'm4a':
                    audio_id= j
                    size=(l)
            si=[]
            for siz,c in zip(s,cod):
                

                if (c != 'mp4a.40.5' or c != 'mp4a.40.2') and (siz is not None and siz != 'NaN'):
                    siz=float(siz)+float(size)
                    si.append(siz)
                else:
                    si.append(siz)
            value = itertools.zip_longest(i,r,si,e,t)
        
            return render(request, 'fb_dow.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})

        elif re.match(regex_reddit,url):
            # print(uploader_url)
            if re.match(regex_youtube, uploader_url):
            
                size=0
                f=[]
                up=[]
                s =len(format_ids)-len(filesize)
                del resolution[0:s] 
                del extension[0:s] 
                del format_ids[0:s] 
            
                
            

                resolution.reverse()
                extension.reverse()
                format_ids.reverse()
                filesize.reverse()
                cod.reverse()
                vbr.reverse()

                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                for i,j in zip(resolution,extension):
                    f.append(i+j)



            
                s=len(resolution)
                s1=len(extension)
                s2=len(format_ids)
                s3=len(filesize)
                s4=len(cod)
                s5= len(vbr)
                

            

                for i,j in enumerate(f):
                    
                    if j not in up:
                        up.append(j)
                    else:
                        # print(i) 3,6,10,11,12
                        resolution.pop(i-s)
                        extension.pop(i-s1)
                        format_ids.pop(i-s2)
                        filesize.pop(i-s3)
                        cod.pop(i-s4)
                        vbr.pop(i-s5)
                
                
                
            
                num = filesize.count(None)
                file_s.reverse()
                c=0
            
                for i,j in enumerate(filesize):
                
                    if j == None:
                        filesize[i]=file_s[-(num-c)]
                        c+=1

            
            
                
                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                audio_id = ''
                for i,r,s,e,c,t in value:
                    if r == 'audio only' and e == 'm4a':
                        audio_id = i
                        size = int(s)
                        print('This is audio size',size)
                

                print(audio_id)
                file_s=[]
                for s,c in zip(filesize,cod):
                    if c != 'mp4a.40.2':
                        s+=size
                        file_s.append(s)
                    else:
                        file_s.append(s)
                
                val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr)
                
                return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
            elif re.match(regex_twitter,uploader_url):

                val = itertools.zip_longest(format_ids,resolution,extension,vbr)
                i=[]
                r=[]
                e=[]
                t=[]
            
                for ids,c,d,tb in val:
                

                    if 'http' in ids or 'source' in ids:
                        i.append(ids)
                    
                        r.append(c)
                        e.append(d)
                        t.append(tb)
                    
                    
                value = itertools.zip_longest(i,r,e,t)
            
                return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
            else:
            
                # print(format_ids)
                # print(resolution)
                # print(extension)
                # print(file_s)
                # print(vbr)
        
                ids=[]
                r=[]
                e=[]
                t=[]
                s=[]
                format_ids.reverse()
                resolution.reverse()
                extension.reverse()
                file_s.reverse()
                vbr.reverse()
                l1=len(format_ids)
                l2=len(resolution)
                l3=len(extension)
                l4=len(file_s)
                l5=len(vbr)
            
                # if l5 == 0:
                #     for i in range(l1):
                #         vbr.append('NaN')
                # elif l1 != l4 and l4 != 0:
                #     for i in range((l1-l4)):
                #         format_ids.pop(-(i+1))
                #         resolution.pop(-(i+1))
                #         extension.pop(-(i+1))
                #         vbr.pop(-(i+1))
            
                val=itertools.zip_longest(format_ids,resolution,extension,file_s,vbr)
                # for ids,res,ext,s,t in val:
                #     print(ids,res,ext,s,t)

                a=0
                audio_id = ''
                for id_,res,ext in zip(format_ids,resolution,extension):
                    if ext == 'mp4' and res == 'audio only':
                        audio_id = id_
                        print(audio_id)
                        a+=1
                        # print(a)

            
                
                for id_,res,ext,size,datarate in val:
                    if a == 1 and (id_[:10] == 'dash-video' or res == 'audio only'):
                    
                        ids.append(id_)
                        r.append(res)
                        e.append(ext)
                        s.append(size)
                        t.append(datarate)
                
                
                    elif a == 0 and ( id_[:10] == 'dash-video' and res != 'audio only'):
                    
                        ids.append(id_)
                        r.append(res)
                        e.append("Without Audio")
                        s.append(size)
                        t.append(datarate)

                    elif a == 0  and len(file_s) == 0:

                        ids.append(id_)
                        r.append(res)
                        e.append(ext)
                        s.append('NaN')
                        t.append(datarate)
        
            
                value= itertools.zip_longest(ids,r,e,s,t)

                return render(request, 'general.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':value})

        elif (re.match(regex_youtube, url) or re.match(regex_khan_acdmy, url)):
            
        
            
            size=0
            f=[]
            up=[]
            s =len(format_ids)-len(filesize)
            del resolution[0:s] 
            del extension[0:s] 
            del format_ids[0:s] 
        
            
        

            resolution.reverse()
            extension.reverse()
            format_ids.reverse()
            filesize.reverse()
            cod.reverse()
            vbr.reverse()

            value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
            for i,j in zip(resolution,extension):
                f.append(i+j)



        
            s=len(resolution)
            s1=len(extension)
            s2=len(format_ids)
            s3=len(filesize)
            s4=len(cod)
            s5= len(vbr)
            

        

            for i,j in enumerate(f):
                
                if j not in up:
                    up.append(j)
                else:
                    # print(i) 3,6,10,11,12
                    resolution.pop(i-s)
                    extension.pop(i-s1)
                    format_ids.pop(i-s2)
                    filesize.pop(i-s3)
                    cod.pop(i-s4)
                    vbr.pop(i-s5)
            
            
            
        
            num = filesize.count(None)
            file_s.reverse()
            c=0
        
            for i,j in enumerate(filesize):
            
                if j == None:
                    filesize[i]=file_s[-(num-c)]
                    c+=1

        
        
            
            value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
            audio_id = ''
            for i,r,s,e,c,t in value:
                if r == 'audio only' and e == 'm4a':
                    audio_id = i
                    size = int(s)
                    print('This is audio size',size)
               

            print(audio_id)
            file_s=[]
            for s,c in zip(filesize,cod):
                if c != 'mp4a.40.2':
                    s+=size
                    file_s.append(s)
                else:
                    file_s.append(s)
             
            val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr)
            
            return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
        
        
            
            
        elif(re.match(regex_twitter, url)):
        
            val = itertools.zip_longest(format_ids,resolution,extension,vbr)
            i=[]
        
            r=[]
            e=[]
            t=[]
        
            for ids,c,d,tb in val:
            

                if 'http' in ids or 'source' in ids:
                    i.append(ids)
                
                    r.append(c)
                    e.append(d)
                    t.append(tb)
                
                
            value = itertools.zip_longest(i,r,e,t)
        
            return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
        elif (re.match(regex_ok_ru,url)):
            index=[]
            for i,j in enumerate(format_ids):
                if j[:3] != 'mpd' and j[:3] != 'hls':
                    index.append(i)
            for i,j in enumerate(index):
                file_s.insert(int(j),'NaN')


            val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr)
            i=[]
            s=[]
            r=[]
            e=[]
            t=[]
            for ids,res,ext,size,tb in val:
            
                if 'mpd' in ids:
                
                    i.append(ids)
                    s.append(size)
                    r.append(res)
                    e.append(ext)
                    t.append(tb)

            value = itertools.zip_longest(i,r,e,s,t)
                    

            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})

        elif (re.match(regex_vimeo,url) or re.match(regex_vimeo,uploader_url)):
        
            
            format_ids.reverse()
            resolution.reverse()
            extension.reverse()
            vbr.reverse()
            cod.reverse()

            
            val = itertools.zip_longest(format_ids,extension,resolution,vbr,cod)
            i=[]
        
        
            e=[]
            r=[]
            t=[]
        
        
            for ids,ext,res,tb,co in val:
                # print(ids,'----',res,'----',ext,'----',tb,'----',co)
                #ids[:28]
                # print(res)
                # print(ids[:29])
                # print(co,ext)
                # print(ext)
            
            
                if  res == "audio only" and ext == 'm4a' and co != 'mp4a.40.2':
                    if ids[:11] == 'dash-akfire':
                        i.append(ids)
                        e.append(ext)
                        r.append(res)
                        t.append(tb)

                    
                    # print(co)
                
                    

                    # i.append(ids)
                
                    # t.append(tb)
                    # e.append(ext)
                    # r.append(res)
                if 'http' in ids or 'source' in ids:
                    i.append(ids)
                
                    t.append(tb)
                    e.append(ext)
                    r.append(res)

            
                
            # print('vimeo')
            
            value = itertools.zip_longest(i,r,e,t)
            return render(request, 'twitter_dow.html', {"title": title,'dur':duration,'thumbnail':thumbnail ,'val': value})
        
        
        elif(re.match(regex_VLive, url)):
            val = itertools.zip_longest(format_ids,resolution,extension,vbr)
            i=[]
        
            r=[]
            e=[]
            t=[]
            for ids,c,d,tr in val:
            

                if 'avc' in ids:
                    i.append(ids)
                
                    r.append(c)
                    e.append(d)
                    t.append(tr)
                
            value = itertools.zip_longest(i,r,e,t)
            return render(request, 'twitter_dow.html', {"title": title, 'thumbnail':thumbnail,'dur':duration,'val': value})

        elif(re.match(regex_SoundCloud, url)):
        
            val = zip(format_ids,resolution,extension)
        

        
            return render(request, 'twitter_dow.html', {"title": title,'thumbnail': thumbnail,'dur':duration,'val':val})

        elif(re.match(regex_daily_motion, url)):
            r_t=[]

            for i, j in zip(resolution, vbr):
                r_t.append(str(i)+' '+str(j)+'kbps')

            val = zip(format_ids,file_s,extension,r_t)
            i=[]
            s=[]
            e=[]
            r=[]
        
            for ids,b,c,d in val:
                if 'http' in ids and '1' in ids:
                    i.append(ids)
                    s.append(b)
                    e.append(c)
                    r.append(d)
        
            value=zip(i,s,e,r)    
            return render(request, 'dow_size.html', {"title": title,'dur':duration, 'thumbnail': thumbnail,'val':value})

        elif(re.match(regex_instagram, url)):
            val = itertools.zip_longest(format_ids,resolution,extension,vbr)
        

        
            return render(request, 'twitter_dow.html', {"title": title,'thumbnail': thumbnail,'dur':duration,'val':val})

        elif (re.match(regex_puhutv,url)):
            r_t=[]
            

            for i, j in zip(resolution, vbr):
                r_t.append(str(i)+' '+str(j)+'kbps')

            val = zip(format_ids,file_s,extension,r_t)
            i=[]
            s=[]
            e=[]
            r=[]
        
            for ids,b,c,d in val:
                if '-1' in ids:
                    i.append(ids)
                    s.append(b)
                    e.append(c)
                    r.append(d)
        
            value=zip(i,s,e,r) 
            return render(request, 'dow_size.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})


        elif (re.match(regex_streamable,url)):
          
            val = itertools.zip_longest(format_ids,resolution,extension,filesize,vbr)
            

            
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})
        elif (re.match(regex_vk,url)):
            if re.match(regex_youtube,uploader_url):
                size=0
                f=[]
                up=[]
                s =len(format_ids)-len(filesize)
                del resolution[0:s] 
                del extension[0:s] 
                del format_ids[0:s] 

                


                resolution.reverse()
                extension.reverse()
                format_ids.reverse()
                filesize.reverse()
                cod.reverse()
                vbr.reverse()

                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                for i,j in zip(resolution,extension):
                    f.append(i+j)




                s=len(resolution)
                s1=len(extension)
                s2=len(format_ids)
                s3=len(filesize)
                s4=len(cod)
                s5= len(vbr)
                



                for i,j in enumerate(f):
                    
                    if j not in up:
                        up.append(j)
                    else:
                        # print(i) 3,6,10,11,12
                        resolution.pop(i-s)
                        extension.pop(i-s1)
                        format_ids.pop(i-s2)
                        filesize.pop(i-s3)
                        cod.pop(i-s4)
                        vbr.pop(i-s5)
                
                
                

                num = filesize.count(None)
                file_s.reverse()
                c=0

                for i,j in enumerate(filesize):
                
                    if j == None:
                        filesize[i]=file_s[-(num-c)]
                        c+=1



                
                value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                audio_id = ''
                for i,r,s,e,c,t in value:
                    if r == 'audio only' and e == 'm4a':
                        audio_id = i
                        size = int(s)
                        print('This is audio size',size)
                    

                print(audio_id)
                file_s=[]
                for s,c in zip(filesize,cod):
                    if c != 'mp4a.40.2':
                        s+=size
                        file_s.append(s)
                    else:
                        file_s.append(s)
                    
                val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr)
                
                return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
            else:

                l1=len(format_ids)
                l2=len(file_s)
                l3=len(resolution)
                l4 = len(extension)
                l5 = len(vbr)
                # print(file_s)
            
                # if l5 == 0:
                #     for i in range(l1):
                #         vbr.insert(i,'NaN')
                
                # if l2 == 0:
                
                #     for i in range(l1):
                #         file_s.insert(i,'NaN')
                # elif l3 == 0:
                #     for i in range(l1):
                #         resolution.insert(i,'NaN')
                # elif l4 == 0:
                #     for i in range(l1):
                #         extension.insert(i,'NaN')
            

                # elif l1 != l2:
                #     for i in range((l1-l2)):
                #         file_s.insert((i),'NaN')
                # elif l1 != l3:
                #     for i in range((l1-l3)):
                #         resolution.insert((i),'NaN')
                # elif l1 != l4:
                #     for i in range((l1-l4)):
                #         extension.insert((i),'NaN')
                # elif l1 != l5:
                #     for i in range((l1-l5)):
                #         vbr.insert((i),'NaN')

                # print(file_s)
                # print(format_ids)
                # print(resolution)
                # print(extension)
                # print(vbr)
                i=[]
                s=[]
                e=[]
                r=[]
                t=[]            
                val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr)
                for ids,res,ext,size,tb in val:
                    if ids[:3] == 'url':
                        # print(size)
                        i.append(ids)
                        r.append(res)
                        e.append(ext)
                        s.append(size)
                        t.append(tb)
                    
                value = zip(i,r,e,t)
                return render(request, 'twitter_dow.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
        elif re.match(regex_espn,url):
            format_ids.reverse()
            resolution.reverse()
            extension.reverse()
            file_s.reverse()
            vbr.reverse()

                        

            

        
            val = zip(format_ids,resolution,extension,file_s,vbr)
            i=[]
            s=[]
            e=[]
            r=[]
            tr=[]
        
            for ids,b,c,d,t in val:
                if 'mezzanine' in ids:
                    i.append(ids)
                    r.append("Full HD")
                    e.append(c)
                    s.append('NaN')
                    tr.append(t) 

                elif 'http' in ids:
                    i.append(ids)
                    r.append(b)
                    e.append(c)
                    s.append(d)
                    tr.append(t)
            value = zip(i,r,e,s,tr)


            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
            
                
        
        
        elif (re.match(regex_tiktok,url)):

            val = zip(format_ids,resolution,extension,filesize,vbr)
            i=[]
            s=[]
            e=[]
            r=[]
            tr=[]
        
            for ids,b,c,d,t in val:
            
                if ('download_addr-0' in ids):

                
                    i.append(ids)
                    s.append(b)
                    e.append('Watermarked')
                    r.append(d)
                    tr.append(t)
                elif ('h264' in ids and ids[-1] == '0'):

                
                    i.append(ids)
                    s.append(b)
                    e.append('No Watermarked')
                    r.append(d)
                    tr.append(t)
            
            value=zip(i,s,e,r,tr)
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})

        elif re.match(regex_ted,url):
            index=[]
            for i,j in enumerate(format_ids):
                if 'hls-audio' in j:
                    index.append(i)
            for i,j in enumerate(index):
                file_s.insert(j,'NaN')
            audio_id=''
            audio_id = format_ids[index[-1]]
            print(audio_id)
            l=len(index)
            for i in range((l-1)):
                format_ids.pop(i)
                resolution.pop(i)
                extension.pop(i)
                file_s.pop(i)
                vbr.pop(i)
            
            value = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr)
        
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})

        elif re.match(regex_cnn,url):
            f=[]
            up=[]
            s=len(resolution)
            s1=len(extension)
            s2=len(format_ids)
            s3=len(file_s)
        
            s5=len(vbr)
            for i,j in zip(resolution,extension):
                    f.append(i+j)
            for i,j in enumerate(f):
                    if j not in up:
                        up.append(j)
                    else:
                        resolution.pop(i-s)
                        extension.pop(i-s1)
                        format_ids.pop(i-s2)
                        file_s.pop(i-s3)
                    
                        vbr.pop(i-s5)

        
            val = zip(format_ids,resolution,extension,file_s,vbr)
                    

            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})
        elif re.match(regex_bili,url):
            
            print('this is bilibili video')
            val = itertools.zip_longest(format_ids,resolution,extension,file_s,vbr,vcodec)
            audio_id=''
            size_=0
            sizee=0
            i=[]
            r=[]
            e=[]
            s=[]
            v=[]
            for ids,res,ext,size,vb,vcd in val:
                # print(ids,'',res,'',ext,'',size,'',vb,'',vcd)
                # if vcd is None:
                #     pass              
                
                if ext == 'm4a' and vcd == 'none':
                    if size not in s:
                        audio_id=ids
                        
                        size_ = size 
                        i.append(ids)
                        r.append(res)
                        e.append(ext)
                        s.append(size)
                        v.append(vb)

                elif vcd is not None and vcd[:4] == 'avc1':
                    i.append(ids)
                    r.append(res)
                    e.append(ext)
                    s.append(size+size_)
                    v.append(vb)
                    

            print(s)        
            value = zip(i,r,e,s,v)

            for ids,res,ext,size,vb in value:
                if ids == audio_id:
                    sizee = size
                
            i_=[]  
            r_=[]  
            e_=[]  
            s_=[]  
            v_=[]
            value = zip(i,r,e,s,v)

            for ids,res,ext,size,vb in value: 
                print(ids,res,ext,size,vb)
                if res == 'audio only':
                    size+=sizee
                    s_.append(size)
                    i_.append(ids)             
                    r_.append(res)             
                    e_.append(ext)             
                    v_.append(vb)
                elif res != 'audio only':
                    i_.append(ids)             
                    r_.append(res)             
                    e_.append(ext)             
                    s_.append(size)
                    v_.append(vb)             
            print(s_)
            print(audio_id)
            # value = zip(i,r,e,s,v)
            # print(r) 
            value = zip(i_,r_,e_,s_,v_)


            
            return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':value})
            
            

        else:
            try:
                print('This is last try block')
                # print('This is uploader url = ',uploader_url)
                if re.match(regex_youtube,uploader_url):
                    # print('this is regex youtube match with uploader url ')
                    f=[]
                    up=[]
                    s =len(format_ids)-len(filesize)
                    del resolution[0:s] 
                    del extension[0:s] 
                    del format_ids[0:s] 
                
                    
                

                    resolution.reverse()
                    extension.reverse()
                    format_ids.reverse()
                    filesize.reverse()
                    cod.reverse()
                    vbr.reverse()

                    value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                    for i,j in zip(resolution,extension):
                        f.append(i+j)



                
                    s=len(resolution)
                    s1=len(extension)
                    s2=len(format_ids)
                    s3=len(filesize)
                    s4=len(cod)
                    s5= len(vbr)
                    

                

                    for i,j in enumerate(f):
                        
                        if j not in up:
                            up.append(j)
                        else:
                            # print(i) 3,6,10,11,12
                            resolution.pop(i-s)
                            extension.pop(i-s1)
                            format_ids.pop(i-s2)
                            filesize.pop(i-s3)
                            cod.pop(i-s4)
                            vbr.pop(i-s5)
                    
                    
                    
                
                    num = filesize.count(None)
                    file_s.reverse()
                    c=0
                
                    for i,j in enumerate(filesize):
                    
                        if j == None:
                            filesize[i]=file_s[-(num-c)]
                            c+=1

                
                
                    
                    value=itertools.zip_longest(format_ids,resolution,filesize,extension,cod,vbr)
                    audio_id = ''

        

                    for i,r,s,e,c,t in value:
                        if r == 'audio only' and e == 'm4a':
                            audio_id = i
                            size = int(s)
                            print('This is audio size',size)
            

                    print(audio_id)
                    file_s=[]
                    for s,c in zip(filesize,cod):
                        if c != 'mp4a.40.2':
                            s+=size
                            file_s.append(s)
                        else:
                            file_s.append(s)

                    if(all(v is None for v in resolution)):
                        return render(request,'errors.html') 
                    else: 
                        val=itertools.zip_longest(format_ids,resolution,file_s,extension,cod,vbr)

                        return render(request, 'yt_download.html', {"title": title, "dur": duration, 'thumbnail':thumbnail,'val':val})
                else:
                    print('This is else function of last try block ')

                # r_t=[]

                # for i, j in zip(resolution, vbr):
                #     r_t.append(str(i)+' '+str(j)+'kbps')
            

            
                    l1=len(format_ids)
                    l2=len(file_s)
                    l3=len(resolution)
                    l4 = len(extension)
                    l5 = len(vbr)
                
                    if l5 == 0:
                        for i in range(l1):
                            vbr.insert(i,'NaN')
                    
                    if l2 == 0:
                    
                        for i in range(l1):
                            file_s.insert(i,'NaN')
                    elif l3 == 0:
                        for i in range(l1):
                            resolution.insert(i,'NaN')
                    elif l4 == 0:
                        for i in range(l1):
                            extension.insert(i,'NaN')
                

                    elif l1 != l2:
                        for i in range((l1-l2)):
                            file_s.insert((i),'NaN')
                    elif l1 != l3:
                        for i in range((l1-l3)):
                            resolution.insert((i),'NaN')
                    elif l1 != l4:
                        for i in range((l1-l4)):
                            extension.insert((i),'NaN')
                    elif l1 != l5:
                        for i in range((l1-l5)):
                            vbr.insert((i),'NaN')

                
                    format_ids.reverse()
                    resolution.reverse()
                    extension.reverse()
                    file_s.reverse()
                    vbr.reverse()
                    # print(file_s)
                    # print(format_ids)
                    # print(resolution)
                    # print(extension)
                    # print(vbr)
                    # print(thumbnail)
                            

                    if(all(v is None for v in resolution)):
                         

                        return render(request,'errors.html')
                    # print("this is thumbnail",thumbnail)
                    else:
                        
                        
                        val = zip(format_ids,resolution,extension,file_s,vbr)


                        return render(request, 'general.html', {"title": title,'thumbnail':thumbnail,'dur':duration,'val':val})

            except:
                print('This is last except block')
                val = zip(format_ids,resolution,extension,vbr)
                return render(request, 'twitter_dow.html', {"title": title,'val':val})
        
    



def error_404(request, exception):
    print('This is 404 error')
    return render(request,'errors.html')
def error_500(request):
    print('This is 500 error')

    return render(request,'errors.html')

def error_403(request,exception):
    print('This is 403 error')

    return render(request,'errors.html')

def error_400(request,exception):
    print('This is 400 error')

    return render(request,'errors.html')


def downloading(request):
    print("This is downloading function")
    if request.method == "POST":
        i=request.POST.get('id')
        ext=request.POST.get('ext')
        print(i)
        print(ext)
        
    
    global url
    print(url)
    global title
    # print(title)
    global audio_id
    print('audio id is = ',audio_id)
    

    if len(title)>100:
        title = title[:50]
        option = {
            'format' : i,
            'outtmpl': f'{title}.{ext}',
        }
    else:
        
        if len(audio_id) != 0:
        
            option = {
                'format':f"{i}+{audio_id}",
                'cachedir': False,
            }
            
        else:
            
            option = {
            'format' : i,
            # 'outtmpl': f'{title}.{ext}',
            'cachedir': False,
            }
            
    
    print(option)
    # print(audio_id)
    # print(title)
    with yt_dlp.YoutubeDL(option) as ydl:
        
        ydl.download([url])
   
    return render(request, 'ytb_main.html')

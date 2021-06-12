import sys, os, subprocess
# This is to get the directory that the program 
# is currently running in.
pwd = os.path.dirname(os.path.realpath(__file__))
videos_list=[]
vid="Videos/"
for root, dirs, files in os.walk(pwd):
    for file in files: 
  
        # change the extension from '.mp3' to 
        # the one of your choice.
        if file.endswith('.mp4'):
            videos_list.append(vid+str(file))
            # vid+=str(file)
# FFMPEG_ENV_PATH = '/ffmpeg_sources/ffmpeg/'
print("file name:",videos_list[0])
#Getting FPS using ffprobe
FPS=30
das_fps=[]
for vids in videos_list:
    print("Video array component", vids)
    FPS=str(subprocess.check_output('ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate ' +vids ,shell=True) )
    print(FPS)
    sp1=FPS.split('/')
    sp2=sp1[0].split("'")
    sp3=sp1[1].split('\\')
    # for tracing
    # print(sp2)
    # print(sp3)
    myfps= float(sp2[1]) / float(sp3[0])
    print(myfps)
    das_fps.append(myfps)

# auxstamp= '00:00:00.00'
# pxlstamp = '00:00:00:01'
# pxlist=pxlstamp.split(':')
# rframe=pxlist[len(pxlist)-1]
# mynum=int(rframe)/myfps
# print(mynum) 
# numstr= str(mynum)
# cat1=numstr.split('.')[1]
# cat2=auxstamp[0:-2]+cat1
# print(cat2)

f = open("input.txt", "r")
timestamp = '00:00:00.00'
c=1
vid_c=0
while(vid_c != len(videos_list)):
    #read next line
    line = f.readline()
    #if line is empty, you are done with all lines in the file
    if not line:
        #EOF reached start processing on new video
        vid_c+=1
        f.seek(0)
        line=f.readline()
    if(vid_c == len(videos_list)):
        break
    #you can access the line
    print(line.strip())
    timestamp= str(line.strip())
    pxlist=timestamp.split(':')
    rframe=pxlist[len(pxlist)-1]
    # print("trace",rframe)
    numerator= int(rframe)
    dominator = das_fps[vid_c]
    mynum=numerator/dominator
    numstr= str(mynum)
    cat1=numstr.split('.')[1]
    cat2=timestamp[0:-3]+'.'+cat1
    # print("trace mycat",cat2)
    subprocess.call('ffmpeg -ss '+ cat2+' -i ' +videos_list[vid_c] +' -frames:v 1 '+'screenshots/screenshot'+str(c)+'.png' +' -noaccurate_seek -y', shell=True)
    c+=1
#close file
f.close()
					
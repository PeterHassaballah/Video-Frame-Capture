import sys, os, subprocess
# This is to get the directory that the program 
# is currently running in.
pwd = os.path.dirname(os.path.realpath(__file__))
vid="Videos/"
for root, dirs, files in os.walk(pwd):
    for file in files: 
  
        # change the extension from '.mp3' to 
        # the one of your choice.
        if file.endswith('.mp4'):
            vid+=str(file)
# FFMPEG_ENV_PATH = '/ffmpeg_sources/ffmpeg/'
print("file name:",vid)
#Getting FPS using ffprobe
FPS=str(subprocess.check_output('ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate ' +vid ,shell=True) )
print(FPS)
sp1=FPS.split('/')
sp2=sp1[0].split("'")
sp3=sp1[1].split('\\')
# for tracing
# print(sp2)
# print(sp3)
myfps= float(sp2[1]) / float(sp3[0])
print(myfps)

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
c=0
while(True):
    #read next line
    line = f.readline()
    #if line is empty, you are done with all lines in the file
    if not line:
        break
    #you can access the line
    print(line.strip())
    timestamp= str(line.strip())
    pxlist=timestamp.split(':')
    rframe=pxlist[len(pxlist)-1]
    mynum=int(rframe)/myfps
    numstr= str(mynum)
    cat1=numstr.split('.')[1]
    cat2=timestamp[0:-3]+'.'+cat1
    print("mycat",cat2)
    c+=1
    subprocess.call('ffmpeg -ss '+ cat2+' -i ' +vid +' -frames:v 1 '+'screenshots/screenshot'+str(c)+'.png' +' -noaccurate_seek -y', shell=True)

#close file
f.close()
					
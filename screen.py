import sys, os, subprocess

# FFMPEG_ENV_PATH = '/ffmpeg_sources/ffmpeg/'
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
    c+=1
    subprocess.call('ffmpeg -ss '+ timestamp+' -i Videos/video.mp4 -frames:v 1 '+'screenshots/screenshot'+str(c)+'.png' +' -noaccurate_seek -y', shell=True)

#close file
f.close()
					
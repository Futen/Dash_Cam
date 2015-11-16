#! /usr/bin/env python

from subprocess import call

video_dir = 'Videos'
for line in open('video_1_to_2_minute.txt','r'):
    line = line.split("\n")[0]
    dir_name = line.split("\t")[0] 
    video_name = dir_name + '.mp4'
    call("ffmpeg -i Videos/%s/%s -r 5 -qscale:v 1 Videos/%s/images/image-%5d.jpg"%(dir_name, video_name, dir_name), shell=True)

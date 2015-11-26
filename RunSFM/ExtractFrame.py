#! /usr/bin/env python
#   This code is to extract frame from each video in the list
import sys
sys.path.append('/home/Futen/Dash_Cam')
from subprocess import call
import SystemParameter

root_dir = SystemParameter.ROOT_PATH
video_dir = SystemParameter.VIDEO_PATH
video_info_file = '%s/video_1_to_2_minute.txt'% root_dir
for line in open(video_info_file,'r'):
    line = line.split("\n")[0]
    dir_name = line.split("\t")[0] 
    video_name = dir_name + '.mp4'
    command = "ffmpeg -i %s/%s/%s -r 5 -qscale:v 1 %s/%s/images/"%(video_dir,dir_name, video_name, video_dir,dir_name) + "image-%5d.jpg"
    call(command, shell=True)
    #######

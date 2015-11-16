#! /usr/bin/env python

import subprocess

video_dir = "/home/kuanting/Dash_Cam/00_download_pre/01_final_videos_HQ/Videos"
f = open("video_1_to_2_minute.txt", "r")
for line in f:
    line = line.split('\t')[0]
    subprocess.call("mkdir -p Videos/%s"%line, shell=True)
    subprocess.call("mkdir -p Videos/%s/images"%line, shell=True)
    subprocess.call("cp /home/Futen/Dash_Cam/config.yaml Videos/%s"%line, shell=True)
    video_name = video_dir + '/' + line + '.mp4'
    subprocess.call("sshpass -p 'k28613966' scp Tesla:%s Videos/%s"%(video_name, line), shell=True)
    '''
    print "start cp " + line
    command = "cp %s/%s/gmm_video/*.jpg Videos/%s/images" %(video_dir, line, line)
    subprocess.call(command, shell=True)
    '''

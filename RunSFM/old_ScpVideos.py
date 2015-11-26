#! /usr/bin/env python

import subprocess

video_dir = "/home/kuanting/Dash_Cam/01_EXP/Videos"
f = open("Videos/video_less_than_one_minute", "r")
for line in f:
    line = line.split('\t')[0]
    subprocess.call("mkdir Videos/%s"%line, shell=True)
    subprocess.call("mkdir Videos/%s/images"%line, shell=True)
    subprocess.call("cp /home/Futen/Dash_Cam/config.yaml Videos/%s"%line, shell=True)
    print "start cp " + line
    command = "cp %s/%s/gmm_video/*.jpg Videos/%s/images" %(video_dir, line, line)
    subprocess.call(command, shell=True)

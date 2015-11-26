#! /usr/bin/env python

import sys
sys.path.append('/home/Futen/Dash_Cam')
from RouteShow import RouteShow
from subprocess import call
import SystemParameter
root_dir = SystemParameter.ROOT_PATH
video_dir = SystemParameter.VIDEO_PATH
f = open("%s/Reconstrction_Check_lst"%root_dir,'r')
lst = []
for line in f:
    line = line.split("\t")
    line[2] = line[2].split('\n')[0]
    if line[2] == 'reconstruction_success':
        lst.append(line[0])
for one in lst:
    print one
    name = '%s/%s/reconstruction.json'%(video_dir,one)
    RouteShow(name)

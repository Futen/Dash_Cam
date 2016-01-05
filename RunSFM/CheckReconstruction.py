#! /usr/bin/env python

import sys
sys.path.append('/home/Futen/Dash_Cam')
from glob import glob
import os
import SystemParameter

video_dir = SystemParameter.VIDEO_PATH
root_dir = SystemParameter.ROOT_PATH

f = open("%s/FINISH_LST.txt" % root_dir, 'r')
f_out = open("%s/Reconstrction_Check_lst.txt" % root_dir, 'w')
for line in f:
    line = line.split("\n")[0]
    arr = line.split("\t")
    name = arr[0]
    if not(os.path.exists("%s/%s/reconstruction.json" % (video_dir, name))):
        print name
        outcome = ''
        img_lst = glob("%s/%s/images/*.jpg" % (video_dir, name))
        match_lst = glob("%s/%s/matches/*.gz" % (video_dir, name))
        if len(img_lst) == len(match_lst):
            outcome = "no_move"
        else:
            outcome = "video_error"
        f_out.write(line+'\treconstruction_fail_%s\n' % outcome)
    else:
        f_out.write(line+'\treconstruction_success\n')
f.close()
f_out.close()

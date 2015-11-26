#! /usr/bin/env python

from glob import glob
import os

f = open("FINISH_LST",'r')
f_out = open("Reconstrction_Check_lst",'w')
for line in f:
    line = line.split("\n")[0]
    arr = line.split("\t")
    name = arr[0]
    if not(os.path.exists("Videos/%s/reconstruction.json"%name)):
        print name
        outcome = ''
        img_lst = glob("Videos/%s/images/*.jpg"%name)
        match_lst = glob("Videos/%s/matches/*.gz"%name)
        if len(img_lst)==len(match_lst):
            outcome = "no_move"
        else:
            outcome = "video_error"
        f_out.write(line+'\treconstruction_fail_%s\n'%outcome)
    else:
        f_out.write(line+'\treconstruction_success\n')
f.close()
f_out.close()

#! /usr/bin/env python

from subprocess import call
from glob import glob
import timeit
import os

'''
call("~/OpenSfM/bin/run_all ~/OpenSfM/data/1", shell=True)
call("~/OpenSfM/bin/run_all ~/OpenSfM/data/2", shell=True)
call("~/OpenSfM/bin/run_all ~/OpenSfM/data/3", shell=True)
'''
finish_lst = []
f_finish = open("FINISH_LST",'r')
try:
    for one in f_finish:
        one = one.split('\t')[0]
        finish_lst.append(one)
except IOError:
    pass
f_finish.close()

video_lst_dir = 'Videos'
video_lst = []
dir_lst = os.listdir("%s/"%video_lst_dir)
for one in dir_lst:
    if os.path.isdir(video_lst_dir + '/' + one):
        video_lst.append(one)

for each in video_lst:
    name = each
    if not(name in finish_lst):
        print name
        start = timeit.default_timer()
        call("/home/Futen/OpenSfM/bin/run_all %s/%s"%(video_lst_dir, name), shell=True)
        stop = timeit.default_timer()
        during = str((stop - start)/60)
        f = open("FINISH_LST",'a')
        f.write("%s\t%s\n"%(name, during))
        f.close()

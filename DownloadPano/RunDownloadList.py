#! /usr/bin/env python

import sys
sys.path.append('/home/Futen/Dash_Cam')
import SystemParameter as SP
import GetCircleBound
import PanoProcess
import subprocess
from multiprocessing import Pool
import numpy as np


info_path = SP.VIDEO_INFO_PATH
video_file = open('%s/video_to_process.txt'%info_path, 'r')

def DownloadList(center):
    pano_lst = []
    bound = GetCircleBound.GetCircleBound(center)
    for latlon in bound:
        pano_name = PanoProcess.GetPanoID(latlon)
        if pano_name != None:
            pano_lst.append((pano_name, latlon[0], latlon[1]))
    return pano_lst
def Download(video_info): # (vname, lat, lon))
    #print video_info_and_path
    vname = video_info[0]
    latlon = (float(video_info[1]), float(video_info[2]))
    path =  SP.GetPath(vname)# get all path

    if path['state']['panolist'] == 'no':
        print vname
        pano_lst = DownloadList(latlon)
        
        f = open('%s/pano_lst.txt'%path['pano_path'], 'w')
        for pano in pano_lst:
        #    print pano
            s = pano[0] + '\t' + str(pano[1]) + '\t' + str(pano[2]) + '\n'
            f.write(s)
        f.close()

if __name__ == '__main__':
    pool = Pool(processes=1)
    video_to_do = []
    for line in video_file:
        line = line.split('\n')[0].split('\t')
        path = SP.GetPath(line[0])
        if path['state']['panolist'] == 'no':
            print line
            video_to_do.append(line)
    print len(video_to_do)
    pool.map(Download, video_to_do)

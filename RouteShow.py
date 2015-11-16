#! /usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import json
import cv2

def optical_center(shot):
    R = cv2.Rodrigues(np.array(shot['rotation'], dtype=float))[0]
    t = shot['translation']
    return -R.T.dot(t)

def RouteShow(name):
    f = open(name, "r")
    obj = json.load(f)
    f.close()
    name_lst = []
    index = 1
    obj = obj[0]
    x_lst = []
    y_lst = []
    z_lst = []
    max_val = 0
    min_val = 0
    x_total = 0
    y_total = 0
    z_total = 0
    while index <= len(obj['shots']):
        name = 'image-%.5d.jpg'%index
        try:
            output = optical_center(obj['shots'][name])
            x_lst.append(output[0])
            y_lst.append(output[1])
            z_lst.append(output[2])
            x_total+=output[0]
            y_total+=output[1]
            z_total+=output[2]
            if max(output) > max_val:
                max_val = max(output)
            if min(output) < min_val:
                min_val = min(output)        
        except KeyError:
            print index
            pass
        index+=1
    fig = plt.figure() # creat a new figure
    ax = fig.gca(projection='3d') # get current figure instance
    ax.scatter(x_lst, y_lst, z_lst)
    x_ava = x_total/len(obj['shots'])
    y_ava = y_total/len(obj['shots'])
    z_ava = z_total/len(obj['shots'])

    print np.shape(x_lst)
    x_lst = np.linspace(min_val, max_val, 100)
    y_lst = []
    z_lst = []
    for i in range(0,100):
        y_lst.append(y_ava)
        z_lst.append(z_ava)
    ax.scatter(x_lst, y_lst, z_lst, s=1,c='r')
    x_lst = []
    y_lst = np.linspace(min_val, max_val, 100)
    z_lst = []
    for i in range(0,100):
        x_lst.append(x_ava)
        z_lst.append(z_ava)
    ax.scatter(x_lst, y_lst, z_lst, s=1,c='r')
    x_lst = []
    y_lst = []
    z_lst = np.linspace(min_val, max_val, 100)
    for i in range(0,100):
        x_lst.append(x_ava)
        y_lst.append(y_ava)
    ax.scatter(x_lst, y_lst, z_lst, s=1,c='r')
    ax.legend()
    plt.show()

#RouteShow(sys.argv[1])

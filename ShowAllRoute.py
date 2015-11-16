#! /usr/bin/env python

from RouteShow import RouteShow
from subprocess import call
f = open("Reconstrction_Check_lst",'r')
lst = []
for line in f:
    line = line.split("\t")
    line[2] = line[2].split('\n')[0]
    if line[2] == 'reconstruction_success':
        lst.append(line[0])
for one in lst:
    print one
    name = 'Videos/%s/reconstruction.json'%one
    RouteShow(name)

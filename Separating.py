
# coding: utf-8
# Author : Sami Ahmad Khan
# University : Illinois Institute of Technology
# CS 430 Project

from operator import itemgetter
import argparse
import glob
import sys
from optparse import OptionParser
import re
import os


# Reading Text File
def read_file(files): 
    with open(files) as file:
        text = file.read().split('\n')
    n = int(text[0]) # Number of points in the file
    points = []
    for t in text[1:]:
        x = int(t.split(' ')[0])
        y = int(t.split(' ')[1])
        points.append((x,y))
    return points,n


# Storing files in the output_greedy folder
def write_output(S,n,fno):
    path = 'output_greedy/greedy_solutionsss'+fno+'.txt'
    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)
    with open(path, 'w') as f:
        sys.stdout = f
        print(n)
        for i in range(0, len(S)):
            print(S[i])
    

# Create union of all the pairs connected to each other
def create_pairs(points):
    U = [] #Containing pairs of all the points
    for i in range(0,len(points)):
        for j in range(i+1, len(points)):
            U.append((points[i],points[j]))
    return U

# Separate all points by minimum number of axises
def separate_points(U,n):
    vAxis = []
    hAxis = []

    #Creating vertical and horizontal axis
    for i in range(1,n):
        vAxis.append(i+0.5)
        hAxis.append(i+0.5)

    S = [] # Solution set
    
    while U!=None:
        count_cutting_V = {} # Number of pairs cut by all vertical axis, stored as key-value
        pairs_per_axis_V = {} # Total pairs per vertical axis
        count_cutting_H = {} # Number of pairs cut by all horizontal axis, stored as key-value
        pairs_per_axis_H = {} # Total pairs per horizontal axis
        max1 = 0
        ver  = [0,0] 
        hor  = [0,0]
        max2 = 0
        U_removed = []
        
        if len(U) == 0:
            break
            
        for v in vAxis:
            count = 0  
            for u in U: 
                if(u[0][0] <v and u[1][0] > v):
                    count += 1
            if(count >= max1):
                max1 = count
                ver[1] = v
                ver[0] = max1
            count_cutting_V.setdefault(v, []).append(count)
        
        for h in hAxis:
            count = 0
            for u in U:
                if((u[0][1] - h) * (u[1][1] - h) < 0):
                    count += 1
            if(count >= max2):
                max2 = count
                hor[1] = h
                hor[0] = max2
            count_cutting_H.setdefault(h, []).append(count)

        
        if(ver[0] > hor[0]):
            S.append('v '+str(ver[1]))
            for u in U: 
                if(((u[0][0] - ver[1]) * (u[1][0] - ver[1])) < 0):
                    U_removed.append(u)
            vAxis.remove(ver[1])

        else:
            S.append('h '+str(hor[1]))
            for u in U:
                if(((u[0][1] - hor[1]) * (u[1][1] - hor[1])) < 0):
                    U_removed.append(u)
            hAxis.remove(hor[1])

        for u in U_removed:
            U.remove(u)

    return S


def main():
    parser = argparse.ArgumentParser() 
    parser.add_argument("--file", "-f", dest="filename")
    parser.add_argument("-n", dest="filenumber",type=str)
    args = parser.parse_args()
    fname = args.filename
    points,n = read_file(args.filename)
    fno = (re.findall("\d+", fname))
    S = separate_points(create_pairs(points),n) 
    print('File Written Successfully')
    write_output(S,len(S),fno[0])
    

if __name__ == "__main__":
    main()




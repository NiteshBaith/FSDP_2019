# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:13:53 2019

@author: Baith
"""

input_avg=input("Enter inputs ")
input_avg=input_avg.split()
input_avg=list(map(int,input_avg))
srt_avg=sorted(input_avg) 
srt_avg.remove(srt_avg[0])
srt_avg.remove(srt_avg[len(srt_avg)-1])
avg=sum(srt_avg)/len(srt_avg)
print(avg)






# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:58:52 2019

@author: Baith
"""
asmt=input("Enter the scored marks in assignments")
A1,A2,A3 = asmt.split()
A1=int(A1)
A2=int(A2)
A3=int(A3)

exam=input("Enter the scored marks in exams")
E1,E2 = exam.split()
E1=int(E1)
E2=int(E2)
weighted_score = ( A1 + A2 + A3 )*0.1 + (E1 + E2 )*0.35
print("weighted score is",weighted_score)

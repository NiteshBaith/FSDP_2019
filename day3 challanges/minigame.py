# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:29:54 2019

@author: Baith
"""
import random as rd
#using random
for i in range(10):
    print(rd.random())
    
for i in range(10):
    print(4*rd.random()+3)
    
# using uniform 
for i in range(10):
    print(rd.uniform(3,7))
# using randint
for i in range(10):
    print(rd.randint(1,10))

# challange 1
    inp=int(input("Enter your guess no:"))
    
    rand=rd.randint(1,10)
    if rand == inp:
        print("You WINS!!!")
    else:
        print("Computer WINS!!")
# challange 2
        print("guess no is:{}\n Comp no is:{}".format(inp,rand))
        
# challange 3
        if abs(inp-rand)>3:
            print("TOO high")
        else:
            print("TOO Close")
# challange 4
            
            i=0
            while(i<10):
                
                 if rand == inp :
                        print("You WINS!!!")
                        break
                 else:
                        inp=int(input("Enter your guess no:"))
                        
# challange 5,6,7,8

                        
inp=input("Enter your guess no:")
r=inp.find('.')
if r==0:
    print ("Enter right number")
else:
    inp=int(inp[:r])
    rand=rd.randint(1,10)
    i=0
    j=6
    if(inp<10):
                while(i<9):
                            i=i+1
                            if rand == inp :  
                                        print("You WINS!!!")
                                        break
                                        
                            else:
                                print("Computer WINS!!")
                                print("guess no is:{} Secret no is:{}".format(inp,rand))
                                print("Tries Left",j-i)
                                inp=int(input("Enter your another guess no:"))
                                if i==5:
                                            print("You have tried max attempts")
                                            break
    else:
        print("Please print value btw 1 t 10")
        
            
        
                     
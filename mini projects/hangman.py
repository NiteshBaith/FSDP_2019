# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import Counter
import random
emptylist=[]
fruit_list = ['banana','apple','grapes','pear','mango','pomegranate','orange','sapodilla','watermalon','muskmalon']
rand_fruit=list(random.choice(fruit_list))
Counter(rand_fruit)
count=0
t=0
emptylist.extend(rand_fruit) #adding all values of rand_fruit in empty list 
print("To Quit the game type quit")
for i in range(len(rand_fruit)):
    emptylist[i]= "_"

print(" ".join(emptylist))

while count<len(rand_fruit):
    if  emptylist==rand_fruit:
        break
    guess_user=input("Enter a guessed letter: ")
    if guess_user in emptylist:
               print("Multipal reptition ")
               count=count-1
               if t==5:
                print("attempts Over...You have lost!!")
                break
    for i in  range(len(rand_fruit)):
        if rand_fruit[i]==guess_user:     #if user values match to random pick
           emptylist[i]=guess_user
           
    if guess_user not in rand_fruit:    #if user value does not match
        if t==5:
            print("attempts Over...You have lost!!")
            break
        count=count-1
        t=t+1
        print("wrong guess!!")
    count=count+1
    
    print(" ".join(emptylist))
print("Well done You have won !!")


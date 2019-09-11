# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:36:19 2019

@author: Baith
"""


def wdc(filename):  
    try:
        fin=open(filename,'r')
        text=fin.read()
        
        fin.close()
        
    except IOError:
            print("file %s not fouund" % filename)
            raise SystemExit
    number_of_characters = len(text)
    number_of_lines = text.count('\n') + 1
    wordlist = text.split(None)
    unique_word=len(set(wordlist))
    number_of_words = len(wordlist)
    print (" number of lines :%d \n number of words: %d \n number of characters: %d \n Unique words: %d \n file name:%s" % (number_of_lines, number_of_words, number_of_characters,unique_word, filename))
    
wdc(filename=input("Enter file name"))
        
        
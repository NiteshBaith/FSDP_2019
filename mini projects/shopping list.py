# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:29:25 2019

@author: Baith
"""

#   Make a list to hold onto our items.
shopping_list = []
new_list = []
# Print out instructions on how to use the app
print ("What should we pick up at the store ?")

while True:
    # ask for new items'
    try:
        new_item = input("> ")
        shopping_list.append(new_item) 
        if  new_item=='':
            print("please pick up a item at least")
            shopping_list.remove(new_item)
        if new_item.upper()=='HELP':
            print("Enter 'SHOW' to showing list items.")
            print ("Enter 'DONE' to stop adding items.")
            print ("Enter 'REMOVE' to remove items.")
            print("> ")
            shopping_list.remove(new_item)
        # be able to quit the app
        if new_item.upper() == 'DONE' or new_item.upper()== 'SHOW' :
            shopping_list.remove(new_item)
            break
        if new_item.upper() == 'REMOVE' :
            if len(shopping_list)==1:
                print("please pick up a item at least because list is empty")
                shopping_list.remove(new_item) 
            else:
                rmv_item=input("Enter the Name of Item you want Remove")
                shopping_list.remove(new_item)
                shopping_list.remove(rmv_item)
        # add new items to our list   
        if "," in new_item:
            shopping_list.remove(new_item)
            new_list=new_item.split(",")
            for each in new_list:
                shopping_list.append(each)               
    except IOError:
                print("The item is not bucket list so cant be removed")
    except Exception:
        print ( "The Name you Enter is wrong please Enter right name to remove")          
#  print out the list
print("Here’s your list")
for item in shopping_list:
    print ( item )
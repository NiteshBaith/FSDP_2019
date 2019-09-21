# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:04:10 2019

@author: Baith
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com

"""
import json

# Reading from a JSON file
with open("jason_file.json", "r") as read_file:
    jsondata=read_file.read()
    print(jsondata)
    # JSON in python data structure 
my_data = json.loads(jsondata)
print ( my_data)
print (my_data['Faculty1']['contact_details'][1]['Residential Address'][1]) # printing  office address
    
# Converts Python Data types to JSON Data Types
new_json_string = json.dumps(my_data)
print (type(new_json_string) )
# Printing jason data in specified formate 

new_json_string = json.dumps(my_data, indent=2 )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2, sort_keys=True)
print (new_json_string)












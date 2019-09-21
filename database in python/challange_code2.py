# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:48:29 2019

@author: Baith
"""

import pymongo

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
#mydb = client.forsk_db

#client = pymongo.MongoClient("mongodb://forsktech:Forsk%40123@cluster0-shard-00-00-tdcf5.mongodb.net:27017,cluster0-shard-00-01-tdcf5.mongodb.net:27017,cluster0-shard-00-02-tdcf5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
#mydb = client.forsk_db

client = pymongo.MongoClient("mongodb+srv://niteshbairwa:niteshmnit@cluster0-ikixl.mongodb.net/test?retryWrites=true&w=majority")
db = client.S2_data



def add_employee(First_Name,Last_name, roll, branch):
    unique_employee = db.S2_collection.find_one({"Roll Number":roll}) # should have unique id so took roll nuber which is must!!
    if unique_employee:
        return "Employee already exists"
    else:
        db.S2_collection.insert_one(
                {
                "Student Name" : First_Name,
                "Last" : Last_name,
                "Roll Number" : roll,
                "Branch Name" : branch
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = db.S2_collection.find()
    for i in user:
        print (i)

#db.S2_collection.drop()
#Insert data in collection
add_employee('Sylvester', 'Fernandes', 1, 'CSE')
add_employee('Yogendra', 'Singh', 2, 'ECE')
add_employee('Rohit', 'Mishra', 3, 'CSE')
add_employee('Kunal', 'Vaid', 4, 'CSE')
add_employee('Devendra', 'Shekhawat', 5, 'ECE')
add_employee('Sylvester', 'Fernandes', 6, 'CSE')
add_employee('Yogendra', 'Singh', 7, 'ECE')
add_employee('Rohit', 'Mishra', 8, 'CSE')
add_employee('Kunal', 'Vaid', 9, 'CSE')
add_employee('Devendra', 'Shekhawat', 10, 'ECE')

fetch_all_employee()
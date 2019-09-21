# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:26:30 2019

@author: Baith
"""
"""
Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3

conn=sqlite3.connect('db_university.db')

#connectiong a cursor
c=conn.cursor()
conn.commit()

c.execute ("""CREATE TABLE uni_tbl(
          Student_Name TEXT,
          Student_Age TEXT,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )"""
          )
#c.execute("DROP TABLE uni_tbl")
conn.commit()

c.execute("INSERT INTO uni_tbl VALUES ('Sylvester', 'Fernandes', 1, 'CSE')")
c.execute("INSERT INTO uni_tbl VALUES ('Yogendra', 'Singh', 2, 'ECE')")
c.execute("INSERT INTO uni_tbl VALUES ('Rohit', 'Mishra', 3, 'CSE')")
c.execute("INSERT INTO uni_tbl VALUES ('Kunal', 'Vaid', 4, 'CSE')")
c.execute("INSERT INTO uni_tbl VALUES ('Devendra', 'Shekhawat', 5, 'ECE')")
c.execute("INSERT INTO uni_tbl VALUES ('Sylvester', 'Fernandes', 6, 'CSE')")
c.execute("INSERT INTO uni_tbl VALUES ('Yogendra', 'Singh', 7, 'ECE')")
c.execute("INSERT INTO uni_tbl VALUES ('Rohit', 'Mishra', 8, 'CSE')")
c.execute("INSERT INTO uni_tbl VALUES ('Kunal', 'Vaid', 9, 'CSE')")
c.execute("INSERT INTO uni_tbl VALUES ('Devendra', 'Shekhawat', 10, 'ECE')")

conn.commit()
c.execute("SELECT * FROM uni_tbl")

print ( c.fetchall() )
from pandas import DataFrame

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["std_Name","Age","Roll NO","Barnch"]
df.to_csv("University_data.csv")
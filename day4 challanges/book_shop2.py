# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:33:16 2019

@author: Baith
"""

list_of_order=[ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
[2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
[3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
[4, ("8732", 7, 10), ("7733",11,10), ("88112", 5, 10)] ]


order_summary = list(map(lambda x: (x[0], x[1][1]*x[1][2] +x[2][1]*x[2][2] + x[3][1]*x[3][2] ) if len(x)==4 
                         else (x[0],x[1][1]*x[1][2] +x[2][1]*x[2][2]), list_of_order))
print(order_summary)


from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
         [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

min_order = 100

invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
print (invoice_totals)

invoice_totals = list(map(lambda x: [x[0]] + [round(reduce(lambda a,b: a + b, x[1:]),2)], invoice_totals))
print (invoice_totals)

invoice_totals = list(map(lambda x: x  if x[1] >= min_order else (x[0], x[1] + 10), invoice_totals))
print (invoice_totals)
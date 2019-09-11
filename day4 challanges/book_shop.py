# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:18:09 2019

@author: Baith
"""
list_of_list=[[34587, 'Learning Python', 'Mark, Lutz',  4, 40.95],
[98762, 'Programming Python', 'Mark Lutz', 5, 56.80],
[77226, 'Head First Python', 'Paul Barry', 3, 32.95],
[88112, 'Einführung in Python3', 'Bernd Klein',  3, 24.9]
]


order_summary = list(map(lambda x: (x[0], round(x[3] * x[4],2)), list_of_list))
print(order_summary)

invoice_totals = list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), order_summary))
print(invoice_totals)


"""list_final2=[]
list_final=[]
i=0
for each in list_of_list:
        list_final.append(list_of_list[i][0])
        for item in each:
            if item==list_of_list[i][3]:
                type(item)
                f=float(item)
                mult=f*list_of_list[i][4]
                list_final2.append(mult)
                
        i=i+1
tuple1=tuple(list_final)
tuple2=tuple(list_final2)
list_got=[(tuple1),(tuple2)]
"""




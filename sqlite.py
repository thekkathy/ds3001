# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:06:27 2021

@author: klemb
"""

import sqlite3

people = [
    ('Jane', 'Doe', 18), 
    ('John', 'Smith', 22), 
    ('Emma', 'Yu', 22), 
    ('Calvin', 'Dew', 24), 
    ('Jake', 'Kim', 18)]

path_to_db = "C:/Users/klemb/Downloads/sqlite-tools-win32-x86-3360000/sqlite-tools-win32-x86-3360000/mydata.db"
conn = sqlite3.connect(path_to_db)
cur = conn.cursor()

# cur.execute('drop table mytable')

#cur.execute('create table mytable (first_name text, last_name text, age real)')
#conn.commit()

#cur.executemany('insert into mytable values (?, ?, ?)', people)
#conn.commit()

for row in conn.execute('select * from mytable'):
    print(row)
  
print()
for row in conn.execute('select * from mytable where age > 20'):
    print(row)
    
print()
for row in conn.execute('select * from mytable group by age'):
    print(row)
    
print()
import pandas as pd
insert_data = []
for row in conn.execute('select * from mytable'):
    insert_data.append(list(row))
df = pd.DataFrame(columns=['first_name', 'last_name', 'age'], data=insert_data)
print(df)


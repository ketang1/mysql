#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(
    host='<hostname>',
    user='<username>',
    password='<password>',
    db='pymysql_db'
)

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM cities;')

    rows = cur.fetchall()

    for (cid, name, population) in rows: 
        print(f"{cid} {name} {population}")
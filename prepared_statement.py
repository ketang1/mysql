#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(
    host='<hostname>',
    user='<username>',
    password='<password>',
    db='pymysql_db'
)

cid = 4

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities WHERE cid=%s", cid)

    cid, name, population = cur.fetchone() 
    print(f"{cid} {name} {population}")
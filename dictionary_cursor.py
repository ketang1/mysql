#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(
    host='<hostname>',
    user='<username>',
    password='<password>',
    db='pymysql_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM cities;')

    rows = cur.fetchall()

    for row in rows: 
        print(f"{row['cid']} {row['name']} {row['population']}")

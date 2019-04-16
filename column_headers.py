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

    desc = cur.description

    print("{0:>3} {1:>10}".format(desc[0][0], desc[1][0]))

    for (cid, name, population) in rows: 
        print("{0:>3} {1:>10}".format(cid, population))
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
    cur.execute('SELECT VERSION()')

    version = cur.fetchone()
    print(f'Database version: {version[0]}')
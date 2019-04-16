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
    cur.execute('''CREATE TABLE cities(
        cid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        population INT NOT NULL)'''
    )
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
    cur.execute('''INSERT INTO cities(name, population)
        VALUES('Bratislava', 432000), ('Budapest', 1759000), ('Prague', 1280000),
            ('Warsaw', 1748000), ('Los Angeles', 3971000), ('New York', 8550000),
            ('Edinburgh', 464000), ('Berlin', 3671000)
    ''')

    conn.commit()
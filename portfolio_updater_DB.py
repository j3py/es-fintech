#!/usr/bin/env python3
# updates postgresql db with portfolio data

import portfolio_consts
import psycopg2

# add SQLAlchemy!!!
# test all the postgres things
# this will have to be changed completely!

try:
    connect_str = portfolio_consts.connect_str
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    cursor.execute("CREATE TABLE portfolio (id serial PRIMARY KEY, name char(40));")
    # run an INSERT statement
    cursor.execute("""INSERT INTO portfolio () VALUES ()""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
    
	
	
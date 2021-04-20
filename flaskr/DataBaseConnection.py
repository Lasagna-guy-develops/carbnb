#!/usr/bin/python3
# coding=utf-8
 
import mysql.connector

#crear la conexión

def connect():
    conn = mysql.connector.connect(host = "localhost",
                                    database = "vaporblack",
                                    user = "root",
                                    password = "Decoldshooterhello12345*",
                                    auth_plugin='mysql_native_password'
                                    )

    
    return conn

def DBInsert(query, var):
    conn = connect()
    
    cur = conn.cursor()
    
    cur.execute(query, var)
    conn.commit()
    conn.close()

def sql_query_var(query, var):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, var)
    rows = cur.fetchall()
    conn.close()
    return rows


def sql_query(query):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows 

#def DBEdit(query, var):

def sql_edit(query, var):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()
    conn.close()
    
def sql_delete(query, var):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()
    conn.close()



if __name__ == "__main__":
    print(getCategories())
    exit()


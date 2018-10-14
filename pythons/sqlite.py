#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error

options = ["Create Table"]

#   Show Options
def show_options():
    for i in options:
        print(i)

def choose_option():
    option = input("choose option: ")
    if int(option) == 1:
        table_details = input("Input Create Table Query: ")
        create_table(conn, table_detail)

#   Database Connection Creator
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

# Task Selector 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


#   Create Table Function 
def create_table(conn, table_name):
     try:
         cur = conn.cursor()
         cur.execute(table_name)
     except Error as e:
         print(e)


#   Main Function
def main():
    database = input("Input Database name: ")
    #connect to database
    conn = create_connection(database)

    show_options()

    while True:
        choose_option()

 

if __name__ == '__main__':
    main()

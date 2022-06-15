from logging import exception
import sqlite3
from sqlite3 import Error

# connection


def sql_connection(name):
    try:
        db_name = sqlite3.connect(name)
        return db_name
    except Error:
        print(Error)

# connection

# make table

# users_informations_table


def users_informations_table(db_name):
    cursorObj = db_name.cursor()
    cursorObj.execute(
        "CREATE TABLE users_informations(id integer PRIMARY KEY, username text,password text)")
    db_name.commit()

# users_informations_table

# user_reports_table


def user_reports_table(user):
    cursorObj = con.cursor()
    cursorObj.execute(
        f"CREATE TABLE {user}_reports(id integer PRIMARY KEY, EorI , grouptype text, price int, date , description text)")
    con.commit()

# user_reports_table


# make table

# insert table

def sql_insert_user(table_name, entities):
    cursorObj = con.cursor()
    cursorObj.execute(
        f'INSERT INTO {table_name}(username, password) VALUES(?, ?)', entities)
    con.commit()


def sql_insert_reports(table_name, entities):
    cursorObj = con.cursor()
    cursorObj.execute(
        f'INSERT INTO {table_name}_reports (EorI, grouptype,price, date , description) VALUES(?, ?, ?, ?, ?)', entities)
    con.commit()


# insert table

# update table

def sql_update(table_name, username, password):
    cursorObj = con.cursor()
    cursorObj.execute(f'UPDATE {table_name} SET password =? where username = ?', [
                      password, username])
    con.commit()

# update table

# select


def select_user_inf(username):
    cursorObj = con.cursor()
    try:
        cursorObj.execute(
            "SELECT username,password FROM users_informations WHERE username=?", (username,))
        row = cursorObj.fetchall()
        return row[0]
    except:
        pass

def select_report(table_name,search_method,wanted):
    columns=["EorI", "grouptype","price", "date" , "description"]
    columns=",".join(columns)
    cursorObj = con.cursor()
    try:
        cursorObj.execute(
            f"SELECT {columns} FROM {table_name}_reports WHERE {search_method}=?", (wanted,))
        row = cursorObj.fetchall()
        return row
    except:
        pass

def sum_EorI(table_name,EorI):
    cursorObj = con.cursor()
    try:
        cursorObj.execute(
            f"SELECT price FROM {table_name}_reports WHERE EorI=?", (EorI))
        row = cursorObj.fetchall()
        a=[]
        for i in row:
            a.append(*i)
        return sum(a)
    except:
        pass

# select


con = sql_connection('users.db')
try:
    users_informations_table(con)
except:
    pass



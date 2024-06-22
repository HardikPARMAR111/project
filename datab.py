import sqlite3
sqlcon=sqlite3.connect("project.db")
cur=sqlcon.cursor()
query="""create table reg_table (
        First_name varchar(50) not null,
        Last_name varchar(50) not null,
        Address varchar(70) not null,
        email varchar(60) not null,
        mobile_no varchar(10) not null,
        User_Id varchar(20) not null,
        Pwd varchar(8) not null
    );"""
print("everything is okay")

    
    
import pymysql

# connection with srver

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

# need to create database

mycursor.execute("create database if not exists python_db")
mydb.commit()

print("Database created successfully")

# connection with database

mydb = pymysql.connect(host="localhost",user="root",password="",database="python_db")
mycursor = mydb.cursor()

# table creation

mycursor.execute("create table student(id int primary key auto_increment, name varchar(40), subject varchar(40))")
mydb.commit()

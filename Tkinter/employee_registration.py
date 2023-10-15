from tkinter import *
from tkinter import messagebox as msg
import mysql.connector

def db_connect():
    return mysql.connector.connect(host = "localhost",user="root", password="",database="tkinter_db")

# to see connection done or not:
# print(db_conncet)

def insertdata():
    if e_name.get()=="" or e_dept=="" or e_salary=="" or e_bonus=="":
        msg.showerror("Insert Status","All Fields are Mandatory")
    else:
        conn = db_connect()
        cursor = conn.cursor()
        query="insert into employee(name,dept,salary,bonus) values(%s,%s,%s,%s)"
        args=(e_name.get(),e_dept.get(),e_salary.get(),e_bonus.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')  # it is used to blank input field after data inserting
        e_dept.delete(0,'end')
        e_salary.delete(0,'end')
        e_bonus.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

def searchdata():
    e_name.delete(0,'end')
    e_dept.delete(0,'end')
    e_salary.delete(0,'end')
    e_bonus.delete(0,'end')
    if e_id.get()=="":
        msg.showerror("Search Status","Id is Mandatory for search Operation")

    else:
        conn=db_connect()
        cursor = conn.cursor()
        query = "select * from employee where id = %s"
        args = (e_id.get(),)
        cursor.execute(query,args)

        row = cursor.fetchall()  # create row to store data from database

        if row:
            for i in row:
                e_name.insert(0,i[1])
                e_dept.insert(0,i[2])
                e_salary.insert(0,i[3])
                e_bonus.insert(0,i[4])
        else:
            msg.showerror("Search Status","ID not found")



root = Tk()

root.geometry("600x500")
root.title("Brijesh")


# pack = use for placing at center
# place used for placing at x and y xoordinates

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)
l_name = Label(root,text="Full Name")
l_name.place(x=50,y=100)
l_dept = Label(root,text="Department")
l_dept.place(x=50,y=150)
l_salary = Label(root,text="Salary")
l_salary.place(x=50,y=200)
l_bonus = Label(root,text="Bonus")
l_bonus.place(x=50,y=250)

e_id = Entry(root)
e_id.place(x=150,y=50)
e_name = Entry(root)
e_name.place(x=150,y=100)
e_dept = Entry(root)
e_dept.place(x=150,y=150)
e_salary = Entry(root)
e_salary.place(x=150,y=200)
e_bonus = Entry(root)
e_bonus.place(x=150,y=250)

# buttons:

insert = Button(root,text="INSERT",bg="black",fg="white",command=insertdata)
insert.place(x=50,y=300)
search = Button(root,text="SEARCH",bg="black",fg="white",command=searchdata)
search.place(x=110,y=300)
update = Button(root,text="UPDATE",bg="black",fg="white")
update.place(x=170,y=300)
delete = Button(root,text="DELETE",bg="black",fg="white")
delete.place(x=230,y=300)

root.mainloop()
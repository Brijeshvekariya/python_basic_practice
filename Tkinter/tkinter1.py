from tkinter import *
from tkinter import messagebox as msg
import mysql.connector

def db_connect():
    return mysql.connector.connect(host = "localhost",user="root", password="",database="tkinter_db")

# to see connection done or not:
# print(db_conncet)

def insertdata():
    if e_fname.get()=="" or e_lname=="" or e_email=="" or e_mobile=="":
        msg.showerror("Insert Status","All Fields are Mandatory")
    else:
        conn = db_connect()
        cursor = conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')  # it is used to blank input field after data inserting
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

def searchdata():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    if e_id.get()=="":
        msg.showerror("Search Status","Id is Mandatory for search Operation")

    else:
        conn=db_connect()
        cursor = conn.cursor()
        query = "select * from student where id = %s"
        args = (e_id.get(),)
        cursor.execute(query,args)

        row = cursor.fetchall()  # create row to store data from database

        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])
        else:
            msg.showerror("Search Status","ID not found")
def updatedata():
    if e_id.get()=="" or e_fname=="" or e_lname=="" or e_email=="" or e_mobile=="":
        msg.showerror("Update Status"<"All Field are Mandatory")
    else:
        conn = db_connect()
        cursor = conn.cursor()
        query="update student set fname=%s,lname=%s,email=%s,mobile=%s where id = %s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        e_fname.delete(0,'end')  # it is used to blank input field after data inserting
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

def deletedata():
    if e_id.get() == "":
        msg.showerror("Delete Status","ID is mandatory")
    else:
        conn = db_connect()
        cursor = conn.cursor()
        query = "delete from student where id = %s"
        args = (e_id.get(),)
        msg.askquestion("Delete Status","Do you want to confirm Delete")
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_id.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")


root = Tk()

root.geometry("600x500")
root.title("Brijesh")


# pack = use for placing at center
# place used for placing at x and y xoordinates

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)
l_fname = Label(root,text="First Name")
l_fname.place(x=50,y=100)
l_lname = Label(root,text="lname")
l_lname.place(x=50,y=150)
l_email = Label(root,text="Email")
l_email.place(x=50,y=200)
l_mobile = Label(root,text="Mobile")
l_mobile.place(x=50,y=250)

e_id = Entry(root)
e_id.place(x=150,y=50)
e_fname = Entry(root)
e_fname.place(x=150,y=100)
e_lname = Entry(root)
e_lname.place(x=150,y=150)
e_email = Entry(root)
e_email.place(x=150,y=200)
e_mobile = Entry(root)
e_mobile.place(x=150,y=250)

# buttons:

insert = Button(root,text="INSERT",bg="black",fg="white",command=insertdata)
insert.place(x=50,y=300)
search = Button(root,text="SEARCH",bg="black",fg="white",command=searchdata)
search.place(x=110,y=300)
update = Button(root,text="UPDATE",bg="black",fg="white",command=updatedata)
update.place(x=170,y=300)
delete = Button(root,text="DELETE",bg="black",fg="white",command=deletedata)
delete.place(x=230,y=300)

root.mainloop()
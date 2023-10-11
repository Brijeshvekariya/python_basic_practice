
import pymysql

# connection with database
mydb = pymysql.connect(host="localhost",user="root",password="",database="python_db")
mycursor = mydb.cursor()

status = True

while status:
    menu = '''
                            MENU

                    1. Store Data
                    2. Veiw Data
                    3. Update Data
                    4. Search Data
                    5. Delete Data

'''
    print(menu)
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        name = input("Enter Your name : ")
        subject = input("Enter subject : ")

        query = "insert into student(name,subject) values(%s,%s)"   # query = "insert into student(name,subject) values('%s','%s')"
        args = (name,subject)
        mycursor.execute(query,args)  # mycursor.execute(query % args) if in query single quote then in excute function we hav to use '%'
        mydb.commit()
        print("data inserted succesfully")
    
    elif(choice == 2):
        query = "select * from student"
        mycursor.execute(query)

        # to fetch data from database
        data = mycursor.fetchall()
        print(data)

    elif(choice == 3):
        try:
            id = int(input("Enter ID: "))
            new_name= input('Enter New Name: ')
            new_subject= input('Enter New Subject: ')
            query = "update student set name = %s,subject = %s where id = %s"
            args = (new_name,new_subject,id)
            mycursor.execute(query,args)
            if mycursor.rowcount>0:  # mycursor.rowcount is used to check how many rows were affected by the UPDATE statement
                mydb.commit()
                print("data updated succesfully")
            else:
                print("Id not found")
        except ValueError:
            print("ID is Mandatory")
    elif(choice == 4):
        # search by name or subject
        try:
            print("1. Search by name \n2. Search by Subject")
            search = int(input("Enter choice : "))
            if search == 1:
                name = input("Enter name : ")
                query = "select * from student where name = %s"
                args=(name)
                mycursor.execute(query,args)
                if mycursor.rowcount>0:  # mycursor.rowcount is used to check how many rows were affected by the UPDATE statement
                    data = mycursor.fetchall()
                    print(data)
                else:
                    print("Name not found")
            elif search==2:
                subject = input("Enter Subject Name : ")
                query = "select * from student where subject = %s"
                args = (subject)
                mycursor.execute(query,args)
                if mycursor.rowcount>0:  # mycursor.rowcount is used to check how many rows were affected by the UPDATE statement
                    data = mycursor.fetchall()
                    print(data)
                else:
                    print("Name not found")
        except:
            ValueError("Name or Subject is Mandatory")
    elif (choice == 5):
        try:
            id = int(input("Enter ID: "))
            query = "delete from student where id = %s"
            args = (id)
            mycursor.execute(query,args)
            if mycursor.rowcount>0:  # mycursor.rowcount is used to check how many rows were affected by the UPDATE statement
                mydb.commit()
                print("data Deleted succesfully")
            else:
                print("Id not found")
        except ValueError:
            print("ID is Mandatory")


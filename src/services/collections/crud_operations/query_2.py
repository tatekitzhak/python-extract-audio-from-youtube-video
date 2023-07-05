#  FOR CREATING RECORDS FUNCTION DEFINITION
def create():
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        while (True):
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            salary = int(input("Enter Salary: "))
            data = (name, age, gender, salary,)
            query = "INSERT into USERS (name, age, gender, salary) VALUES (?, ?, ?,?)"
            cursor.execute(query, data)
            con.commit()
            ch = input("Do You want to Add More Records(Y/N): ")
            if ch == "N" or ch == "n":
                cursor.close()
                break
            else:
                pass
    except:
        print("Error in Record Creation")

# FOR READING ONE RECORD FUNCTION DEFINITION
def read_one():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    ids = int(input("Enter Your ID: "))
    query = "SELECT * from USERS WHERE id = ?"
    result = cursor.execute(query, (ids,))
    if (result):
        for i in result:
            print(f"Name is: {i[1]}")
            print(f"Age is: {i[2]}")
            print(f"Salary is: {i[4]}")
    else:
        print("Roll Number Does not Exist")
        cursor.close()

# FOR READING ALL RECORDS FUNCTION DEFINITION
def read_all():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    query = "SELECT * from USERS"
    result = cursor.execute(query)
    if (result):
        print("\n<===Available Records===>")
        for i in result:
            print(f"Name is : {i[1]}")
            print(f"Age is : {i[2]}")
            print(f"Salary is : {i[4]}\n")
    else:
        pass
    
# FOR UPDATING RECORDS FUNCTION DEFINITION
def update():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    idd = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    salary = int(input("Enter Salary: "))
    data = (name, age, gender, salary, idd,)
    query = "UPDATE USERS set name = ?, age = ?, gender = ?, salary = ? WHERE id = ?"
    result = cursor.execute(query, data)
    con.commit()
    cursor.close()
    if (result):
        print("Records Updated")
    else:
        print("Something Error in Updation")

# FOR DELETING RECORDS FUNCTION DEFINITION
def delete():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    idd = int(input("Enter ID: "))
    query = "DELETE from USERS where ID = ?"
    result = cursor.execute(query, (idd,))
    con.commit()
    cursor.close()
    if (result):
        print("One record Deleted")
    else:
        print("Something Error in Deletion")

# MAIN BLOCK
try:
    while (True):
        print("1). Create Records: ")
        print("2). Read Records: ")
        print("3). Update Records: ")
        print("4). Delete Records: ")
        print("5). Exit")
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            create()
        elif ch == 2:
            print("1). Read Single Record")
            print("2). Read All Records")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                read_one()
            elif choice == 2:
                read_all()
            else:
                print("Wrong Choice Entered")
        elif ch == 3:
            update()
        elif ch == 4:
            delete()
        elif ch == 5:
            break
        else:
            print("Enter Correct Choice")
except:
    print("Database Error")

#END
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="employee"
)
mycursor = mydb.cursor()

print("\n1.New Profile 2.Read Profiles 3.Update Profile 4.Delete Profile")
a = int(input("Enter a choice:"))

if a == 1:
    o = str(input("Enter your Employee ID:"))
    p = str(input("Enter your name:"))
    q = str(input("Enter your Job title:"))
    r = str(input("Enter your salary:"))
    s = str(input("Enter your City:"))
    sql = "INSERT INTO e_file (E_id,Name,Title,Salary,City) VALUES (%s,%s,%s,%s,%s)"
    val = (o, p, q, r, s)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

elif a == 2:
    mycursor.execute("SELECT* FROM e_file ")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

elif a==3:
    d = str(input("Enter your Employee ID:"))
    print("\n1.Name  2.Title 3.Salary 4.City")
    f = int(input("Enter a choice:"))

    if f == 1:
        m = str(input("Enter new name:"))
        upd = ("UPDATE e_file SET Name = %s WHERE E_id= %s")
        var = (m , d)
        mycursor.execute(upd , var)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected.")

    elif f == 2:
        m = str(input("Enter new Title:"))
        upd = ("UPDATE e_file SET Title = %s WHERE E_id= %s")
        var = (m , d)
        mycursor.execute(upd , var)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected.")

    elif f == 3:
        m = str(input("Enter new salary:"))
        upd = ("UPDATE e_file SET Salary = %s WHERE E_id= %s")
        var = (m , d)
        mycursor.execute(upd , var)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected.")

    elif f == 4:
        m = str(input("Enter new City:"))
        upd = ("UPDATE e_file SET City = %s WHERE E_id= %s")
        var = (m , d)
        mycursor.execute(upd , var)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected.")

    else:
        print("Invalid choice!")

elif a == 4:
    c = int(input("Enter your Employee ID:"))
    code = ("DELETE FROM e_file WHERE E_id = %s ")
    emp = (c,)
    mycursor.execute(code, emp)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted.")

    mycursor.execute("SELECT* FROM e_file ")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

else:
    print("Invalid choice!")

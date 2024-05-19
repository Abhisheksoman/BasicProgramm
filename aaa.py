print("\n1.New Profile 2.Read Profile 3.Update Profile 4.Delete Profile")
a=int(input("Enter a choice:"))

if a==1:
    p=str(input("Enter your name:"))
    q=str(input("Enter your Job title:"))
    r=int(input("Enter your salary:"))
    s=str(input("Enter your address:"))
    sql = "INSERT INTO efile (Name,Title,Salary,Address) VALUES (%s,%s,%d,%s)"
    val=(p,q,r,s)
    mycursor.executemany(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

elif a==2:
    b=str(input("Enter your Employee ID"))
    mycursor.execute("SELECT* FROM efile WHERE Eid=",b)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

elif a==3:
    print("Do you want to change your profile")

elif a==4:
    c=int(input("Enter your Employee ID:"))
    mycursor.execute("DELETE FROM emp_file WHERE E_id=",c)

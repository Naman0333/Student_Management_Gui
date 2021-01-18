#import Li
import tkinter as tk
from tkinter import messagebox
import sqlite3

#---------------------------Create Connection to Database---------------------------------------------
def  connection():
    try:
        conn=sqlite3.connect('student.db')
    except:
        print("Can't connect the datebase")
    return conn


#-----------------------------------verifier the Empty Fields-----------------------------------------
def verifier():
    a=b=c=d=e=f=g=h=i=0
    if not name.get():
        textarea.insert(tk.END,"<>Student Name is Required<>\n")
    if not fname.get():
        textarea.insert(tk.END,"<>Father Name is Required<>\n")
    if not age.get():
        textarea.insert(tk.END,"<>Student Age is Required<>\n")
    if not roll.get():
        textarea.insert(tk.END,"<>Student Roll No. is Required<>\n")
    if not phone.get():
        textarea.insert(tk.END,"<>Student Phone is Required<>\n")
    if not aadhar.get():
        textarea.insert(tk.END,"<>Student Aadhar is Required<>\n")
    if not address.get():
        textarea.insert(tk.END,"<>Student Address is Required<>\n")
    if not email.get():
        textarea.insert(tk.END,"<>Student Email is Required<>\n")
    if not course.get():
        textarea.insert(tk.END,"<>Course is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1:
        return  1
    else:
        return 0


#------------------------------------------- Add new student Record---------------------------------------
def add_student():
    ret = verifier()
    if ret ==0:
        conn=connection()
        mycursor=conn.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS Students(Name VARCHAR(30),Father_Name VARCHAR(30),Age INT,ROll_No INT PRIMARY KEY,Phone BIGINT,Aadhar BIGINT,Address Text,Email VARCHAR(30),Course VARCHAR(30))")
        query1 = "INSERT INTO Students(Name,Father_Name,Age,ROll_No,Phone,Aadhar,Address,Email,Course) VALUES(?,?,?,?,?,?,?,?,?)"
        values = name.get(),fname.get(),int(age.get()),int(roll.get()),int(phone.get()),int(aadhar.get()),address.get(),email.get(),course.get()
        mycursor.execute(query1,values)
        conn.commit()
        conn.close()
        textarea.insert(tk.END,"New Student Added Sucessfully!!\n")
        reset()

#--------------------------------------View Students Records-------------------------------------
def view_student():
    conn = connection()
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Students")
    data =mycursor.fetchall()
    for i in data:
        textarea.insert(tk.END,str(i)+"\n")
    conn.commit()
    conn.close()

#---------------------------------------Update Student Record----------------------------------------
def update_student():
    ret = verifier()
    if ret==0:
        conn = connection()
        mycursor = conn.cursor()
        quary = "UPDATE Students SET Name=?,Father_Name=?,Age=?,Roll_No=?,Phone=?,Aadhar=?,Address=?,Email=?,Course=? WHERE Roll_No=?"
        values=(name.get(),fname.get(),int(age.get()),int(roll.get()),int(phone.get()),int(aadhar.get()),address.get(),email.get(),course.get(),int(roll.get()))
        mycursor.execute(quary,values)
        conn.commit()
        conn.close()
        textarea.insert(tk.END,"Update Record Successfully!!\n")
        reset()

#------------------------------------------Delete Student Record-------------------------------------------
def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE Roll_No=?",(int(roll.get()),))
        conn.commit()
        conn.close()
        textarea.insert(tk.END,"SUCCESSFULLY DELETED THE USER\n")
        reset()

#-------------------------------------------Reset the all Entry fields----------------------------------------------------------
def reset():
    name_entry.delete(0,tk.END)
    fname_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    roll_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    aadhar_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    course_entry.delete(0,tk.END)


#-------------------------------------------Quit the Application---------------------------------------------------------------
def quit():
    exit = tk.messagebox.askyesnocancel("Student Management System","Do you want exit?")
    if exit:
        window.destroy()

#-----------------------------------------Window,Logo,Window Name--------------------------------------------------------------
window = tk.Tk()
window.title("Student Management System")
window.geometry("900x480+0+0")
window.resizable(False,False)

#-----------------------------------------------textvariable----------------------------------------------------
name=tk.StringVar()
fname=tk.StringVar()
age=tk.StringVar()
roll=tk.StringVar()
phone=tk.StringVar()
aadhar=tk.StringVar()
address=tk.StringVar()
email=tk.StringVar()
course=tk.StringVar()


#------------------------------------------------Create the Labels----------------------------------------------------
name_label = tk.Label(window,text="Name")
fname_label = tk.Label(window,text="Father Name")
age_label = tk.Label(window,text="Age")
roll_label = tk.Label(window,text="Roll No.")
phone_label = tk.Label(window,text="Phone")
aadhar_label = tk.Label(window,text="Aadhar")
address_label = tk.Label(window,text="Address")
email_label = tk.Label(window,text="Email")
course_label = tk.Label(window,text="Course")

#-----------------------------------------------Place the Labels---------------------------------------------------
name_label.place(x=0,y=0)
fname_label.place(x=0,y=30)
age_label.place(x=0,y=60)
roll_label.place(x=0,y=90)
phone_label.place(x=0,y=120)
aadhar_label.place(x=0,y=150)
address_label.place(x=0,y=180)
email_label.place(x=0,y=210)
course_label.place(x=0,y=240)

#---------------------------------------------Create Entry for Labels----------------------------------------------
name_entry = tk.Entry(window,width=20,textvariable=name)
fname_entry = tk.Entry(window,width=20,textvariable=fname)
age_entry = tk.Entry(window,width=20,textvariable=age)
roll_entry = tk.Entry(window,width=20,textvariable=roll)
phone_entry = tk.Entry(window,width=20,textvariable=phone)
aadhar_entry = tk.Entry(window,width=20,textvariable=aadhar)
address_entry = tk.Entry(window,width=20,textvariable=address)
email_entry = tk.Entry(window,width=20,textvariable=email)
course_entry = tk.Entry(window,width=20,textvariable=course)

#--------------------------------------------place all the entry---------------------------------------------------
name_entry.place(x=100,y=0)
fname_entry.place(x=100,y=30)
age_entry.place(x=100,y=60)
roll_entry.place(x=100,y=90)
phone_entry.place(x=100,y=120)
aadhar_entry.place(x=100,y=150)
address_entry.place(x=100,y=180)
email_entry.place(x=100,y=210)
course_entry.place(x=100,y=240)

name_entry.focus()
#----------------------------------------textarea-----------------------------------------------------------------
textarea= tk.Text(window,width=80,height=20)
textarea.grid(row=10,column=3)

#--------------------------------------create all button----------------------------------------------------------
add_button = tk.Button(window,text="Add",width=35,command=add_student)
view_button = tk.Button(window,text="View",width=35,command=view_student)
update_button = tk.Button(window,text="Update",width=35,command=update_student)
delete_button = tk.Button(window,text="Delete",width=35,command=delete_student)
reset_button = tk.Button(window,text="Reset",width=35,command=reset)
Quit_button = tk.Button(window,text="Quit",width=35,command=quit)

#---------------------------------------Grid all Buttons-----------------------------------------------------------
add_button.grid(row=11,column=0,)
view_button.grid(row=12,column=0)
update_button.grid(row=13,column=0)
delete_button.grid(row=14,column=0)
reset_button.grid(row=15,column=0)
Quit_button.grid(row=16,column=0)


window.mainloop()
from tkinter import *
import tkinter.messagebox as msg
import MySQLdb as mysql
from tkinter.ttk import *
import tkinter as tk

window=Tk()
window.geometry("600x600")
window.title("Registration Window")

def insert():
    name=e_name.get();
    uname=e_uname.get();
    pwd=e_pwd.get();
    gen=c_gen.get();
    dob_dd=c_dd.get();
    dob_mm=c_mm.get();
    dob_yyyy=c_yy.get();
    address=e_add.get();
    pin=e_pin.get();
    phone=e_phn.get();
    mail=e_mail.get();
    nat=c_nat.get();

    if(name=="" or uname=="" or pwd=="" or gen=="" or dob_dd=="" or dob_mm=="" or dob_yyyy=="" or address=="" or pin=="" or phone=="" or mail=="" or nat==""):
        msg.showinfo("Insert Status","All Fields are Required")
    else:
        con = mysql.connect(user="root", password="",host='localhost', database="student")
        cursor=con.cursor()
        cursor.execute("insert into student_details values('"+ name +"','"+ uname +"','"+ pwd +"','"+ gen +"','"+ dob_dd +"','"+ dob_mm +"','"+ dob_yyyy +"','"+ address +"','"+ pin +"','"+ phone +"','"+ mail +"','"+ nat +"')")
        cursor.execute("commit");

        e_name.delete("0","end");
        e_uname.delete("0","end");
        e_pwd.delete("0","end");
        c_gen.current(0);
        c_dd.current(0);
        c_mm.current(0);
        c_yy.current(0);
        e_add.delete("0","end")
        e_pin.delete("0","end")
        e_phn.delete("0","end");
        e_mail.delete("0","end");
        c_nat.current(0);
        msg.showinfo("Insert Status","Inserted Successfully")
        con.close();

def clr():
    e_name.delete("0","end");
    e_uname.delete("0","end");
    e_pwd.delete("0","end");
    c_gen.current(0);
    c_dd.current(0);
    c_mm.current(0);
    c_yy.current(0);
    e_add.delete("0","end")
    e_pin.delete("0","end")
    e_phn.delete("0","end");
    e_mail.delete("0","end");
    c_nat.current(0);

def login():
    
    window_1=Toplevel(window)
    window_1.geometry("400x400")
    window_1.title("Login Window")

    def login_verify():
        uname=e_uname_1.get();
        pwd=e_pwd_1.get();
        con = mysql.connect(user="root", password="",host='localhost', database="student")
        cursor=con.cursor()
        cursor.execute("select uname,pwd from student_details where uname='{}' and pwd='{}'".format(uname,pwd))
        
        res=cursor.fetchone()
        if not res:
            msg.showinfo("Login Status","Invalid Login Credentials")
        elif res[0]==uname and res[1]==pwd:
            msg.showinfo("Login Status","Login Successful")
            def display():
                reg=Tk()
                con = mysql.connect(user="root", password="",host='localhost', database="student")
                cursor=con.cursor()
                cursor.execute("select * from student_details where uname='{}' and pwd='{}'".format(uname,pwd))
                res=cursor.fetchone()
                
                
            display()
                
    
    #TITLE
    name_1=Label(window_1,text="STUDENT LOGIN",font=('Bold',18))
    name_1.place(x=100,y=0)

    #USER_NAME
    uname_1=Label(window_1,text="Username",font=('Bold',20))
    uname_1.place(x=70,y=70)

    #PASSWORD
    pwd_1=Label(window_1,text="Password",font=('Bold',20))
    pwd_1.place(x=73,y=100)

    e_uname_1=Entry(window_1)
    e_uname_1.place(x=205,y=80)

    e_pwd_1=Entry(window_1)
    e_pwd_1.place(x=205,y=110)
    
    #LOGIN BUTTON
    sub=Button(window_1,text="Login",width=20,command=login_verify)
    sub.place(x=130,y=205)

    window_1.mainloop()
    

#TITLE
name=Label(window,text="STUDENT REGISTRATION",font=('Bold',18))
name.place(x=0,y=0)

#NAME
name=Label(window,text="Name",font=('Bold',18))
name.place(x=115,y=40)

#USER_NAME
uname=Label(window,text="Username",font=('Bold',18))
uname.place(x=70,y=70)

#PASSWORD
pwd=Label(window,text="Password",font=('Bold',18))
pwd.place(x=73,y=100)

#GENDER
gen=Label(window,text="Gender",font=('Bold',18))
gen.place(x=96,y=130)

#DATE_OF_BIRTH
dob=Label(window,text="DOB",font=('Bold',18))
dob.place(x=120,y=160)

#ADDRESS
add=Label(window,text="Address",font=('Bold',18))
add.place(x=86,y=190)

#PIN
pin=Label(window,text="PIN Code",font=('Bold',18))
pin.place(x=74,y=250)

#PHONE NUMBER
phn=Label(window,text="Phone Number",font=('Bold',18))
phn.place(x=12,y=280)

#EMAIL
mail=Label(window,text="Email",font=('Bold',18))
mail.place(x=110,y=310)

#NATIONALITY
nat=Label(window,text="Nationality",font=('Bold',18))
nat.place(x=57,y=340)



e_name=Entry(window)
e_name.place(x=185,y=45)

e_uname=Entry(window)
e_uname.place(x=185,y=75)

e_pwd=Entry(window,show="*")
e_pwd.place(x=185,y=105)

c_gen=Combobox(window,width=10)
c_gen['values']=('select','Male','Female','Others')
c_gen.current(0)
c_gen.place(x=185,y=135)

c_dd=Combobox(window,width=5)
c_dd['values']=('DD','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
c_dd.current(0)
c_dd.place(x=185,y=165)
c_mm=Combobox(window,width=5)
c_mm['values']=('MM','01','02','03','04','05','06','07','08','09','10','11','12')
c_mm.current(0)
c_mm.place(x=245,y=165)
c_yy=Combobox(window,width=10)
c_yy['values']=('YYYY','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021')
c_yy.current(0)
c_yy.place(x=305,y=165)

e_add=Entry(window)
e_add.place(x=185,y=195,height=50,width=180)

e_pin=Entry(window,width=10)
e_pin.place(x=185,y=255)

e_phn=Entry(window)
e_phn.place(x=185,y=285)

e_mail=Entry(window,width=35)
e_mail.place(x=185,y=315)

c_nat=Combobox(width=10)
c_nat['values']=('select','Indian','Others')
c_nat.current(0)
c_nat.place(x=185,y=345)

#SUBMIT BUTTON
sub=Button(window,text="Submit",width=10,command=insert)
sub.place(x=155,y=405)

#CLEAR BUTTON
clr_B=Button(window,text="Clear",width=10,command=clr)
clr_B.place(x=235,y=405)

#EXISTING BUTTON
ex=Button(window,text="Existing User ?",width=20,command=login)
ex.place(x=315,y=405)

window.mainloop()

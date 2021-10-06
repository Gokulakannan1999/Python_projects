from tkinter import *
from tkinter import messagebox
import MySQLdb as p
def student():
    A=E1.get();
    B=E2.get();
    C=E3.get();
    D=E4.get();
    E=E5.get();
    F=E6.get();
    G=E7.get();
    H=E8.get();
    if (A==" "or B==" "or C==" "or D==" "or E==" "or F==" "or G==" "or H==" "):
        messagebox.showinfo("insert all details successfully")
    else:
        db=p.connect("localhost","root","","akash123")
        print("connected")
        cur=db.cursor()
        #cur.execute("create table apr2002(Studentregisternumber varchar(30),Studentname varchar(30),Tamilmark varchar(30),Englishmark varchar(30),Mathsmark varchar(30),Sciencemark varchar(30),Socialmark varchar(30),Total varchar(30))")
        cur.execute("insert into apr2002 values(' " + A + " ',' " + B +" ',' "+ C +" ',' "+ D +" ',' "+ E +" ',' "+ F +" ',' "+ G +" ',' "+ H +" ')")
        cur.execute("commit")
        
        db.close()
def marks():
    global E1,E2,E3,E4,E5,E6,E7,E8
    if len(E1.get())<10:
        messagebox.showerror('user','To give a large REGISTER NUMBER')
    elif len(E1.get())>10:
        messagebox.showerror('user','INVALID REGISTER NUMBER')
    elif E2.get().isdigit():
        messagebox.showerror('user','Enter Only ALPHABETS')
    elif E2.get().islower():
        messagebox.showerror('user','Enter Only Capital Letters like(ABC)')
    elif len(E2.get())>12:
        messagebox.showerror('user','Enter Name BELOW 12 Letters')
    elif len(E2.get())<5:
        messagebox.showerror('user','Enter Name ABOVE  5 Letters')
    elif int(E3.get())>100:
        messagebox.showerror('user','Enter the correct TAMILMARK')
    elif int(E4.get())>100:
        messagebox.showerror('user','Enter the correct ENGLISHMARK')
    elif int(E5.get())>100:
        messagebox.showerror('user','Enter the correct MATHSMARK')
    elif int(E6.get())>100:
        messagebox.showerror('user','Enter the correct SCIENCEMARK')
    elif int(E7.get())>100:
        messagebox.showerror('user','Enter the correct SOCIALMARK')
    elif int(E3.get())<0:
        messagebox.showerror('user','Enter the POSITIVE Tamilmark')
    elif int(E4.get())<0:
        messagebox.showerror('user','Enter the POSITIVE Englishmark')
    elif int(E5.get())<0:
        messagebox.showerror('user','Enter the POSITIVE Mathsmark')
    elif int(E6.get())<0:
        messagebox.showerror('user','Enter the POSITIVE Sciencemark')
    elif int(E7.get())<0:
        messagebox.showerror('user','Enter the POSITIVE Socialmark')
    else:
        TAMIL=int(Tamilmark.get())
        ENGLISH=int(Englishmark.get())
        MATHS=int(Mathsmark.get())
        SCIENCE=int(Sciencemark.get())
        SOCIAL=int(Socialmark.get())
        TOTAL=TAMIL+ENGLISH+MATHS+SCIENCE+SOCIAL
        Total.set(TOTAL)
        messagebox.showinfo('user','REGISTERED SUCCESSFULLY')
        

window=Tk()
window.title("STUDENT MARK REGISTRATION")
window.geometry("1350x250")
window.configure(bg="Black")
lb1=Label(window,width=25,text="STUDENTREGISTERNUMBER",font=("Chiller",20),fg="blue",bg="white")
lb1.place(x=40,y=60)
lb2=Label(window,width=25,text="STUDENTNAME",font=("Chiller",20),fg="blue",bg="white")
lb2.place(x=40,y=100)
lb3=Label(window,width=25,text="TAMILMARK",font=("Chiller",20),fg="blue",bg="white")
lb3.place(x=40,y=140)
lb4=Label(window,width=25,text="ENGLISHMARK",font=("Chiller",20),fg="blue",bg="white")
lb4.place(x=40,y=180)
lb5=Label(window,width=25,text="MATHSMARK",font=("Chiller",20),fg="blue",bg="white")
lb5.place(x=40,y=220)
lb6=Label(window,width=25,text="SCIENCEMARK",font=("Chiller",20),fg="blue",bg="white")
lb6.place(x=40,y=260)
lb7=Label(window,width=25,text="SOCIALMARK",font=("Chiller",20),fg="blue",bg="white")
lb7.place(x=40,y=300)
lb8=Label(window,width=25,text="TOTAL",font=("Chiller",20),fg="blue",bg="white")
lb8.place(x=40,y=340)

Studentregisternumber=StringVar()
Studentname=StringVar()
Tamilmark=StringVar()
Englishmark=StringVar()
Mathsmark=StringVar()
Sciencemark=StringVar()
Socialmark=StringVar()
Total=IntVar()



E1=Entry(window,width=30,textvariable=Studentregisternumber)
E1.place(x=300,y=90)
A=E1.get()
E2=Entry(window,width=30,textvariable=Studentname)
E2.place(x=300,y=130)
B=E2.get()
E3=Entry(window,width=30,textvariable=Tamilmark)
E3.place(x=300,y=150)
C=E3.get()
E4=Entry(window,width=30,textvariable=Englishmark)
E4.place(x=300,y=200)
D=E4.get()
E5=Entry(window,width=30,textvariable=Mathsmark)
E5.place(x=300,y=230)
E=E5.get()
E6=Entry(window,width=30,textvariable=Sciencemark)
E6.place(x=300,y=290)
F=E6.get()
E7=Entry(window,width=30,textvariable=Socialmark)
E7.place(x=300,y=320)
G=E7.get()
E8=Entry(window,width=30,textvariable=Total)
E8.place(x=300,y=360)
H=E8.get()
B1=Button(window,text="SUBMIT",command=marks)
B1.place(x=300,y=390)
B2=Button(window,text="CONFIRM",command=student)
B2.place(x=300,y=440)

 














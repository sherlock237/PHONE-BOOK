from Tkinter import*
from tkMessageBox import *
import sqlite3
import re
from datetime import date
currentdate=date.today().strftime('%Y')
currentdate=int(currentdate)
age=currentdate-18
age=int(age)
globall=[1]
globall1=[1]
mn=0
def first():
    root=Tk()
    root.geometry("700x900")
    root.config(bg="light yellow")
    Label(root,text="PROJECT TITLE: PhoneBook",font="none 16 bold").place(x=2,y=3)
    Label(root,text="Project of Python and database",font="none 16 bold").place(x=200,y=50)
    Label(root,text="Developed By: Achal Bhadada",font="none 16 bold",fg="blue").place(x=230,y=100)
    Label(root,text="Enroll No.: 181B012",font="none 16 bold",fg="blue").place(x=280,y=140)
    Label(root,text="****************************",fg="blue",font="none 16 bold").place(x=250,y=180)
    Label(root,text="make mouse movement over this screen to close",font="none 16 bold",fg="red").place(x=140,y=420)
    aa=PhotoImage(file="ju.gif")
    bb=Label(root,image=aa)
    bb.place(x=300,y=240)
    def close(e=1):
        root.destroy()
    root.bind("<Motion>",close)
    root.mainloop()
first()
con=sqlite3.Connection('PHONE BOOK')
cur=con.cursor()
root=Tk()
root.title('Phone Book')
root.config(bg="light blue")
root.geometry("540x900")
a=PhotoImage(file="iconfinder_phone_1807538.gif")
b=Label(root,image=a)
b.place(x=200,y=0)
Label(root,text='PHONE RECORDS',fg='blue',bg="light blue",font='none 20 bold underline').place(x=130,y=130)
cur.execute("create table if not exists detail(ID INTEGER primary key AUTOINCREMENT ,fname varchar(20),mname varchar(20),lname varchar(20),website varchar(20),company  varchar(20),DOB date,pincode number(6),city varchar(20),state varchar(20))")
cur.execute("create table if not exists phone_detail(phone_ID int references detail(ID) on delete cascade,phone_type varchar(20) ,phoneno integer(10),primary key(phone_ID,phoneno))")
cur.execute("create table if not exists email_detail(email_ID int references detail(ID) on delete cascade,Email_Type varchar(20) ,EmailId varchar(20), primary key(email_ID,EmailId))")
Label(root,text='First Name',fg='black',bg='light blue',font='none 17 bold ').place(x=30,y=180)
Label(root,text='Middle Name',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=210)
Label(root,text='Last Name',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=240)
Label(root,text='Website',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=270)
Label(root,text='Company',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=300)
Label(root,text='Date of Birth',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=330)
Label(root,text='*Date format dd-mm-yyyy',fg='red',bg='light blue',font='none 8 bold').place(x=398,y=333)
Label(root,text='Pincode',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=360)
Label(root,text='City',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=390)
Label(root,text='State',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=420)
Label(root,text='Select Phone Type',fg='dark green',bg='light blue',font='none 17 bold').place(x=30,y=460)
Label(root,text='Phone Number',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=492)
def add():
    e15=Entry(root)
    e15.place(x=270,y=553)
    v12=IntVar()
    mn=e15.get()
    Label(root,text='Select Phone Type',fg='dark green',bg='light blue',font='none 17 bold').place(x=30,y=520)
    Label(root,text='Phone Number',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=550)
    Radiobutton(root,text="Office",font="none 11 bold",variable=v12,value=1,bg='light blue').place(x=270,y=523)
    Radiobutton(root,text="Home",font="none 11 bold",variable=v12,value=2,bg='light blue').place(x=350,y=523)
    Radiobutton(root,text="Mobile",font="none 11 bold",variable=v12,value=3,bg='light blue').place(x=430,y=523)
Button(root,text='+',font='none 10 bold',command=add).place(x=400,y=495)
Label(root,text='Select Email Type',fg='dark green',bg='light blue',font='none 17 bold').place(x=30,y=580)
Label(root,text='Email Id',fg='black',bg='light blue',font='none 17 bold').place(x=30,y=620)
ee=Entry(root)
ee.place(x=270,y=183)
e1=Entry(root)
e1.place(x=270,y=213)
e2=Entry(root)
e2.place(x=270,y=243)
e3=Entry(root)
e3.place(x=270,y=273)
e4=Entry(root)
e4.place(x=270,y=303)
e5=Entry(root)
e5.place(x=270,y=333)
e6=Entry(root)
e6.place(x=270,y=363)
e7=Entry(root)
e7.place(x=270,y=393)
e8=Entry(root)
e8.place(x=270,y=423)
e9=Entry(root)
e9.place(x=270,y=498)
e10=Entry(root)
e10.place(x=270,y=623)
def remove():
    i22=0
    qqq2=1
    qqq3=1
    qqq4=1
    count=0
    while i22==0:
        try:
            a,b,c,d,e,f,g,h,i,j,k=ee.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),int(e9.get()),e10.get()
            qqq=len(e9.get())
            qqq1=len(a)
            qqq21=len(b)
            qqq31=len(c)
            kkk=len(k)
            pin=len(g)
            for uu in range (0,qqq1):
                if a[uu].isdigit()==True:
                    qqq2=0
            for uu in range (0,qqq21):
                if b[uu].isdigit()==True:
                    qqq3=0
            for uu in range (0,qqq31):
                if c[uu].isdigit()==True:
                    qqq4=0
                    
            if pin>6:
                showinfo('Error','Pincode length reached')
                e6.delete(0,END)
                i22=i22-1
                continue
            if type(g)!=int and pin!=0:
                showinfo('Error','Invalid Pincode')
                e6.delete(0,END)
                i22=i22-1
                continue
            if a==b:
                showinfo('Error','First name and Middle name should not be same')
                i22=i22-1
                ee.delete(0,END)
                e1.delete(0,END)
                continue
            if b==c and qqq31!=0 :
                showinfo('Error','Middle name and Last name should not be same')
                i22=i22-1
                e1.delete(0,END)
                e2.delete(0,END)
                continue
            if a==c:
                showinfo('Error','First name and Last name should not be same')
                i22=i22-1
                e1.delete(0,END)
                e2.delete(0,END)
                continue
            if qqq>15 :
                showinfo('Error','phone number limit reached')
                i22=i22-1
                e9.delete(0,END)
                continue
            if qqq2==0:
                showinfo('Error','Invalid Name')
                i22=i22-1
                ee.delete(0,END)
                continue
            if qqq3==0:
                showinfo('Error','Invalid Name')
                i22=i22-1
                e1.delete(0,END)
                continue
            if qqq4==0:
                showinfo('Error','Invalid Name')
                i22=i22-1
                e2.delete(0,END)
                continue
            if qqq1==0:
                showinfo('Error','First name should not be Empty')
                i22=i22-1
                ee.delete(0,END)
                continue
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if (re.search(regex,k)):
                count=count+1
            if count==0 and kkk!=0:
                showinfo('Error','Please enter a valid email address')
                i22=i22-1
                e10.delete(0,END)
                continue
            if len(f)!=0:
                date,month,year=f.split('-')
                year=int(year)
                if year>age:
                    showinfo('Error','you are not above 18 or you have entered wrong date format ')
                    i22=i22-1
                    e5.delete(0,END)
                    continue
               
            cur.execute("insert into detail(fname,mname,lname,website,company,dob,pincode,city,state) values(?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i))
            cur.execute("insert into phone_detail(phone_ID,phone_type,phoneno) values((select max(ID) from detail),?,?)",(z,j))
            cur.execute("insert into email_detail(email_ID,Email_Type,EmailId) values((select max(ID) from detail),?,?)",(o,k))
            ee.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)
            con.commit()
            cur.execute("select * from detail")
            print cur.fetchall()
            cur.execute("select * from phone_detail")
            print cur.fetchall()
            cur.execute("select * from email_detail")
            print cur.fetchall()
            showinfo("Save","record successfully saved")
            i22=i22+1
        except ValueError:
            showinfo('Error','Invalid phone number')
            i22=i22-1
            e9.delete(0,END)
            continue
def new():
    root=Tk()
    root.geometry("750x900")
    root.config(bg="light blue")
    Label(root,text="Searching Phone book",font="none 16 bold").place(x=250,y=5)
    Label(root,text="Enter Name to Search",font="none 16 bold").place(x=20,y=50)
    E=Entry(root)
    E.place(x=260,y=55,width=250)
    l=Listbox(root,width=700,height=700,font="none 16 bold")
    l.config(bg="light pink")
    l.place(x=0,y=100)
    #yy2=cur.execute('select fname,mname,lname from detail order by fname').fetchall()
    #for i in yy2:
        #l.insert(END,i)
    def des():
        root.destroy()
    Button(root,text="close",font="none 10 bold",command=des).place(x=250,y=650)
    
    def se(event):
        if ord(event.char)==8:
            lll=len(E.get())-1
            E.delete(lll,END)
        else:
            E.insert(END,event.char)      
        a=[1]
        a[0]=['%'+E.get()+'%']
        l.delete(0,END)
        cur.execute('select * from detail where fname like (?)',a[0])
        x=cur.fetchall()
        globall=[1]
        for ii in x:
            globall.append(ii)
        for i in x:
            u=i[1]+' ' +i[2]+' ' +i[3]
            l.insert(END,u)
        def ldisplay(event):
            l=event.widget
            selection=int(l.curselection()[0])
            print globall[selection+1][0]
            root1=Tk()
            root1.geometry('750x900')
            lbb=Listbox(root1,width=750,height=750,font="none 16 bold")
            lbb.place(x=0,y=50)
            lbb.config(bg='orange')
            Label(root1,text='INFORMATION',font='none 16 bold').place(x=250,y=5)
            root1.config(bg='yellow')
            def dele():
                cur.execute('delete from detail where id=?',(globall[selection+1][0],))
                con.commit()
                showinfo("Delete",'Contact Deleted Succesfully')
                root1.destroy()
                des()
            def back():
                root1.destroy()
            Button(root1,text="Close",font="none 10 bold",command=back).place(x=50,y=650)
            Button(root1,text="Delete",font="none 10 bold",command=dele).place(x=250,y=650)
            cur.execute('select fname,mname,lname,website,company,dob,pincode,city,state,phone_type,phoneno,Email_Type,EmailId from detail d inner join email_detail ed on d.ID=ed.email_ID inner join phone_detail pd on d.ID=pd.phone_ID where d.ID=(?)',(globall[selection+1][0],))
            fetch=cur.fetchall()
            print fetch
            end=0
            tup=['FIRST NAME','MIDDLE NAME','LAST NAME','WEBSITE','COMPANY','DATE OF BIRTH','PINCODE','CITY','STATE','PHONE TYPE','PHONE NUMBER','EMAIL TYPE','EMAIL ID']
            
            for i in fetch:
                for j in i:
                    lbb.insert(end,str(tup[end])+'         :         '+str(j))
                    end=end+1
        l.bind('<<ListboxSelect>>',ldisplay)
    root.bind_all('<Key>',se)
    
def destroy():
    root.destroy()
#  ****************************************************    EDIT    ****************************************************************
def ed():
    root=Tk()
    root.geometry("700x900")
    root.config(bg="silver")
    Label(root,text="EDIT PANEL",font="none 16 bold").place(x=250,y=5)
    Label(root,text="Enter Name to Search",font="none 16 bold").place(x=20,y=50)
    E1=Entry(root)
    E1.place(x=260,y=55,width=250)
    l1=Listbox(root,width=700,height=700,font="none 16 bold")
    l1.config(bg="light pink")
    l1.place(x=0,y=100)
    def ba():
        root.destroy()
    Button(root,text="Close",font="none 10 bold",command=ba).place(x=250,y=650)
    def see(event):
        
        if ord(event.char)==8:
                lll1=len(E1.get())-1
                E1.delete(lll1,END)
        else:
            E1.insert(END,event.char)   
        aa=[1]
        aa[0]=['%'+E1.get()+'%']
        l1.delete(0,END)
        cur.execute('select * from detail where fname like (?)',aa[0])
        x1=cur.fetchall()
        globall1=[1]
        for ii in x1:
            globall1.append(ii)
        for i in x1:
            u1=i[1]+' ' +i[2]+' ' +i[3]
            l1.insert(END,u1)
        def ldisplayy(event):
            
            l1=event.widget
            selection1=int(l1.curselection()[0])
            print globall1[selection1+1][0]
            root2=Tk()
            root2.geometry('540x900')
            root2.config(bg='silver')
            Label(root2,text='Edit Panel',font='none 16 bold').place(x=230,y=5)
            Label(root2,text='First Name',fg='black',bg='silver',font='none 17 bold ').place(x=30,y=180)
            Label(root2,text='Middle Name',fg='black',bg='silver',font='none 17 bold').place(x=30,y=210)
            Label(root2,text='Last Name',fg='black',bg='silver',font='none 17 bold').place(x=30,y=240)
            Label(root2,text='Website',fg='black',bg='silver',font='none 17 bold').place(x=30,y=270)
            Label(root2,text='Company',fg='black',bg='silver',font='none 17 bold').place(x=30,y=300)
            Label(root2,text='Date of Birth',fg='black',bg='silver',font='none 17 bold').place(x=30,y=330)
            Label(root2,text='Pincode',fg='black',bg='silver',font='none 17 bold').place(x=30,y=360)
            Label(root2,text='City',fg='black',bg='silver',font='none 17 bold').place(x=30,y=390)
            Label(root2,text='State',fg='black',bg='silver',font='none 17 bold').place(x=30,y=420)
            Label(root2,text='Select Phone Type',fg='dark green',bg='silver',font='none 17 bold').place(x=30,y=460)
            Label(root2,text='Phone Number',fg='black',bg='silver',font='none 17 bold').place(x=30,y=500)
            Label(root2,text='Select Email Type',fg='dark green',bg='silver',font='none 17 bold').place(x=30,y=540)
            Label(root2,text='Email Id',fg='black',bg='silver',font='none 17 bold').place(x=30,y=580)
            ee1=Entry(root2)
            ee1.place(x=270,y=183)
            e11=Entry(root2)
            e11.place(x=270,y=213)
            e21=Entry(root2)
            e21.place(x=270,y=243)
            e31=Entry(root2)
            e31.place(x=270,y=273)
            e41=Entry(root2)
            e41.place(x=270,y=303)
            e51=Entry(root2)
            e51.place(x=270,y=333)
            e61=Entry(root2)
            e61.place(x=270,y=363)
            e71=Entry(root2)
            e71.place(x=270,y=393)
            e81=Entry(root2)
            e81.place(x=270,y=423)
            e91=Entry(root2)
            e91.place(x=270,y=503)
            e101=Entry(root2)
            e101.place(x=270,y=583)
            v11=IntVar()
            Radiobutton(root2,text="Office",font="none 11 bold",variable=v1,value=1).place(x=270,y=463)
            Radiobutton(root2,text="Home",font="none 11 bold",variable=v1,value=2).place(x=350,y=463)
            Radiobutton(root2,text="Mobile",font="none 11 bold",variable=v1,value=3).place(x=430,y=463)
            v21=IntVar()
            if v11.get()==1:
                z1='Office'
            elif v11.get()==2:
                z1='Home'
            else:
                z1='Mobile'

            Radiobutton(root2,text="Office",font="none 11 bold",variable=v2,value=1).place(x=270,y=543)
            Radiobutton(root2,text="Personal",font="none 11 bold",variable=v2,value=2).place(x=350,y=543)
            if v21.get()==1:
                o1='Office'
            else:
                o1='Personal'
            cur.execute('select fname,mname,lname,website,company,dob,pincode,city,state,phoneno,EmailId from detail d inner join email_detail ed on d.ID=ed.email_ID inner join phone_detail pd on d.ID=pd.phone_ID where d.ID=(?)',(globall1[selection1+1][0],))
            records=cur.fetchall()
            for t in records:
                ee1.insert(0,t[0])
                e11.insert(0,t[1])
                e21.insert(0,t[2])
                e31.insert(0,t[3])
                e41.insert(0,t[4])
                e51.insert(0,t[5])
                e61.insert(0,t[6])
                e71.insert(0,t[7])
                e81.insert(0,t[8])
                e91.insert(0,t[9])
                e101.insert(0,t[10])
            def sss():
                a4=[ee1.get(),e11.get(),e21.get(),e31.get(),e41.get(),e51.get(),e61.get(),e71.get(),e81.get(),globall1[selection1+1][0]]
                cur.execute("update detail set fname=?,mname=?,lname=?,website=?,company=?,dob=?,pincode=?,city=?,state=? where ID=?",a4)
                a5=[e91.get(),globall1[selection1+1][0]]
                cur.execute("update phone_detail set phoneno=? where phone_ID=?",a5)
                a6=[e101.get(),globall1[selection1+1][0]]
                cur.execute("update email_detail set EmailId=? where email_ID=?",a6)
                showinfo('update',"Contact updated sucessfully")
                con.commit()
                root2.destroy()
                root.destroy()
                
            Button(root2,text="Save",font="none 10 bold",command=sss).place(x=30,y=660)
            def cl():
                root2.destroy()
            Button(root2,text='Close',font='none 10 bold',command=cl).place(x=250,y=660)
        l1.bind('<<ListboxSelect>>',ldisplayy)
    root.bind_all('<Key>',see)

    
Button(root,text="Save",font="none 10 bold",command=remove).place(x=30,y=660)
Button(root,text="Search",font="none 10 bold",command=new).place(x=250,y=660)
Button(root,text="Close",font="none 10 bold",command=destroy).place(x=340,y=660)
Button(root,text="Edit",font="none 10 bold",command=ed).place(x=450,y=660)
v1=IntVar()
Radiobutton(root,text="Office",font="none 11 bold",variable=v1,value=1,bg='light blue').place(x=270,y=463)
Radiobutton(root,text="Home",font="none 11 bold",variable=v1,value=2,bg='light blue').place(x=350,y=463)
Radiobutton(root,text="Mobile",font="none 11 bold",variable=v1,value=3,bg='light blue').place(x=430,y=463)
v2=IntVar()
if v1.get()==1:
    z='Office'
elif v1.get()==2:
    z='Home'
else:
    z='Mobile'

Radiobutton(root,text="Office",font="none 11 bold",variable=v2,value=1,bg='light blue').place(x=270,y=583)
Radiobutton(root,text="Personal",font="none 11 bold",variable=v2,value=2,bg='light blue').place(x=350,y=583)
if v2.get()==1:
    o='Office'
else:
    o='Personal'
 
root.mainloop()

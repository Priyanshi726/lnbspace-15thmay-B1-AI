from tkinter import* 
import sqlite3
 
root = Tk()
root.geometry('600x500')
root.title("Registration Form")
root.configure(background="powder blue") 
 
Fullname=StringVar()
Email=StringVar()
Phone=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
 
 
 
def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   phone=Phone.get()
   course=c.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Phone TEXT,course TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Phone,COURSE) VALUES(?,?,?,?,?,?)',(name1,email,gender,country,phone,course))
   conn.commit()
    
    
              
label_0 = Label(root, text="REGISTRATION FORM",width=20,font=("bold", 20))
label_0.place(x=110,y=30)
 
 
label_1 = Label(root, text="FULLNAME",width=20,font=("bold", 10))
label_1.place(x=60,y=130)
 
entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=270,y=130)
 
label_2 = Label(root, text="EMAIL",width=20,font=("bold", 10))
label_2.place(x=60,y=180)
 
entry_2 = Entry(root,textvar=Email)
entry_2.place(x=270,y=180)
 
label_3 = Label(root, text="GENDER",width=20,font=("bold", 10))
label_3.place(x=60,y=230)
 
Radiobutton(root, text="MALE",padx = 5, variable=var, value=1).place(x=270,y=230)
Radiobutton(root, text="FEMALE",padx = 20, variable=var, value=2).place(x=350,y=230)
 
label_4 = Label(root, text="COUNTRY",width=20,font=("bold", 10))
label_4.place(x=60,y=280)
 
list1 = ['India','Canada','Nepal','London','Singapore','Germany'];
 
droplist=OptionMenu(root,c, *list1)
droplist.config(width=18,fg='blue')
c.set("Choose your country") 
droplist.place(x=270,y=280)
 
label_5 = Label(root, text="PHONE",width=20,font=("bold", 10))
label_5.place(x=60,y=330)

entry_5 = Entry(root,textvar=Phone)
entry_5.place(x=270,y=330)

label_6 = Label(root, text="COURSE",width=20,font=("bold", 10))
label_6.place(x=60,y=380)
 
list2 = ['ML','AI','Python','C++','Java','Cloud'];
 
droplist=OptionMenu(root,d, *list2)
droplist.config(width=18,fg='blue')
d.set("Choose your course") 
droplist.place(x=270,y=370)
 

var2= IntVar()

Button(root, text='SUBMIT',width=20,bg='blue',fg='black',font=("bold", 12),command=database).place(x=160,y=450)
 
root.mainloop()

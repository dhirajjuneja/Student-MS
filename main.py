from logging import DEBUG
from tkinter import *
from tkinter import ttk
from  datetime import date
from tkinter import filedialog
import shutil
import os
from tkinter import Text, Tk,messagebox,PhotoImage
import json
import requests
import pyrebase
# import TkTreectrl as treect


firebaseConfig={
    "apiKey": "none",
    "authDomain": "tdaybefore.firebaseapp.com",
    "databaseURL": "https://tdaybefore-default-rtdb.firebaseio.com",
    "projectId": "tdaybefore",
    "storageBucket": "tdaybefore.appspot.com",
    "messagingSenderId": "none",
    "appId": "none",
    "measurementId": "none"
}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()



today=date.today()
print ('software is runing......')
firstw=Tk()
firstw.title("Student Admin Pannel")
firstw.geometry("1600x1000+0+0")
label=Label(text="Student Admin Pannel",font=("times new roman",35),bg="#F7CAC9")
label.pack(side=TOP ,fill=X)
user1=Label(text="USERNAME",font=("arial",23))
user1.place(x=610,y=120)
user=Entry(width=17,bd=5,font=("arial",20))
user.place(x=570,y=200)
label.pack(side=TOP ,fill=X)
user2=Label(text="PASSWORD",font=("arial",23))
user2.place(x=610,y=280)
user3=Entry(width=17,show="*",bd=5,font=("arial",20))
user3.place(x=570,y=360)
student_url = 'https://tdaybefore-default-rtdb.firebaseio.com/students.json'
admin_url = 'https://tdaybefore-default-rtdb.firebaseio.com/admin.json'
fire_visitor_url = 'https://tdaybefore-default-rtdb.firebaseio.com/visitors.json'

def second(admin_username):
    global secondw
    secondw=Tk()
    secondw.title("Student Admin Pannel")
    secondw.geometry("1600x1000+0+0")
    def distroy4():
        secondw.destroy()
        root(admin_username)
    def student():
        student1=Tk()
        student1.title("STUDENT DETAILS")
    def studentid(admin_username):
        rot = Tk()
        rot.title("VISITORS")
        rot.geometry("1600x1000+0+0")
        def distroy():
            rot.destroy()
            second(admin_username)
        mainlabel = Label(rot, text="STUDENT DETAILS", font=("times new roman", 35), bg="#F7CAC9")
        mainlabel.pack(side=TOP, fill=X)
        backbutton2=Button(rot, text="<< BACK",width=17,font=("arial", 17), bg="#FF6F61",command=distroy)
        backbutton2.place(x=0,y=0)
        chat1 = ttk.Treeview(rot,height=20, columns=('name','sur','fee','branch'), selectmode="extended")
        chat1.heading('#0', text='ID', anchor=CENTER)
        chat1.heading('#1', text=' NAME', anchor=W)
        chat1.heading('#2', text='FEES', anchor=W)
        chat1.heading('#3', text='COURSE', anchor=W)
        chat1.heading('#4', text="LAST NAME", anchor=W)
        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#3', stretch=YES, minwidth=100, width=200)
        chat1.column('#4', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=100)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        chat1.place(x=470, y=130)
        ttk.Style().configure("Treeview", background="#ffff72", foreground="black")
        ttk.Style().configure("Treeview.Heading", background="blue", foreground="palevioletRed1")
        

        vsb=ttk.Scrollbar(rot, orient="vertical",command=chat1.yview)
        vsb.place(x=1027,y=150,height=400+20)
        chat1.configure(yscrollcommand=vsb.set)

        request  = requests.get(student_url)
        data = request.json()
        # print(data)
        # print(data.keys())
        for key in data:
            # print(key)
            if key == 'visitors' or key == 'admin':
                pass
            else:
                # print(data[f'{key}']['fees'])
                chat1.insert('',0,text=f'{key}',values=(data[f'{key}']['f_name'], data[f'{key}']['fees'], data[f'{key}']['branch'], data[f'{key}']['l_name']))


    def viewenquiry2(admin_username):
        rt = Tk()
        rt.title("VISITORS")
        rt.geometry("1600x1000+0+0")
        def destroy():
            rt.destroy()
            second(admin_username)
        mainlabel =Label(rt, text="VISITOR", font=("times new roman", 35), bg="#F7CAC9")
        mainlabel.pack(side=TOP, fill=X)
        chat1 = ttk.Treeview(rt,height=20 , columns=('EMAIL', 'ENQUIRY', 'DATE'), selectmode="extended")
        chat1.heading('#0', text='NAME', anchor=CENTER)
        chat1.heading('#1', text='PHONE', anchor=CENTER)
        chat1.heading('#2', text='PURPOSE', anchor=CENTER)
        chat1.column('#1', stretch=YES, minwidth=50, width=100)
        chat1.column('#2', stretch=YES, minwidth=50, width=300)
        chat1.column('#0', stretch=YES, minwidth=50, width=70)
        vsb = ttk.Scrollbar(rt, orient="vertical", command=chat1.yview)
        backbutton=Button(rt, text="<< BACK",width=17,font=("arial", 17), bg="#FF6F61",command=destroy)
        backbutton.place(x=0,y=0)
        vsb.place(x=835, y=170, height=400 + 20)
        chat1.configure(yscrollcommand=vsb.set)
        chat1.place(x=400, y=170, width=450)
        ttk.Style().configure("Treeview", background="#ffff72", foreground="black")
        ttk.Style().configure("Treeview.heading", background="blue", foreground="white")

        request  = requests.get(fire_visitor_url)
        data = request.json()
        # print(data)
        # print(data.keys())
        for key in data:
            if key == 'visitors':
                pass
            else:
                # print(data)
                chat1.insert('',0,text=data[f'{key}']['v_name'],values=(data[f'{key}']['v_phone'], data[f'{key}']['v_purpose']))

    def distroy5():
        secondw.destroy()
        window(admin_username)
    def distroy6():
        secondw.destroy()
        enquiry1(admin_username)
    def distroy7():
        secondw.destroy()
        viewenquiry2(admin_username)
    def distroy8():
        secondw.destroy()
        studentid(admin_username)
    admin_username = str.title(admin_username)
    mainlabel= Label(secondw,text="Student Admin Pannel", font=("times new roman", 35), bg="#F7CAC9")
    mainlabel.pack(side=TOP, fill=X)
    mainlabel2= Label(secondw,text=f"Welcome {admin_username}", font=("times new roman", 35), justify=CENTER, bg="#817D49", fg="white")
    mainlabel2.pack(side=LEFT, expand=True, fill=X)
    button = Button(secondw,width=13, font=("arial", 20), text="REGISTRATION", bg="#92A8D1", command=distroy4)
    button.place(x=10, y=480)
    enquiry = Button(secondw, width=13, font=("arial", 20), text="FEE DETAILS", bg="#92A8D1",command=distroy5)
    enquiry.place(x=260, y=480)
    fee_details = Button(secondw, width=13, font=("arial", 20), text="VISTOR ENTRY", bg="#92A8D1",command=distroy6)
    fee_details.place(x=500, y=480)
    viewenquiry= Button(secondw, width=13, font=("arial", 20), text="VISITOR BOARD", bg="#92A8D1",command=distroy7)
    viewenquiry.place(x=740, y=480)
    viewenquiry1 = Button(secondw, width=13, font=("arial", 20), text="STUDENT ID ", bg="#92A8D1",command=distroy8)
    viewenquiry1.place(x=990, y=480)


	
	


def distroy():
    firstw.destroy()
def login():
    request  = requests.get(admin_url)
    data = request.json()
    if user.get() not in data:
        t = messagebox.showerror("INVALID USERNAME ", "YOU HAVE ENTERED INVALID USERNAME")
        user.delete(0,END)
        user3.delete(0,END)
    else:
        if user3.get() != data[f'{user.get()}']['password']:
            t = messagebox.showerror("INVALID PASSWORD ", "YOU HAVE ENTERED INVALID PASSWORD")
        else:
            second(data[f'{user.get()}']['name'])
            distroy()









def root(admin_username):
    root=Tk()
    root.geometry("1600x1000+0+0")
    root.title("Student Admin Pannel")
    global entry1
    global entry2
    global entry3
    global entry4
    global entry5
    global user_name
    global box
    global name
    global radio1
    global radio2
    name = StringVar()
    global sur
    sur = StringVar()
    global gander
    gander = IntVar()
    global var1
    var1 = IntVar()
    global var2
    var2 = IntVar()
    global branch
    branch = StringVar()
    global rollno
    rollno = StringVar()
    global email
    email = StringVar()
    global course
    course = StringVar()
    global python
    python = IntVar()
    global java
    java = IntVar()
    global c
    c = IntVar()
    global d
    d = IntVar()
    global calculate
    calculate = StringVar()
    global calculate_rollno
    calculate_rollno = StringVar()
    id = IntVar()
    search = IntVar()

    NAME = name.get()
    SUR = sur.get()
    EMAIL = email.get()
    BRANCH = branch.get()
    GANDER = gander.get()
    PYTHON = python.get()
    JAVA = java.get()
    C = c.get()
    D = d.get()
    CALCULATE = calculate.get()
    CALCULATE_ROLLNO = calculate_rollno.get()
    calculation2 = 2000
    label=Label(root,text="REGISTRATION FORM", font=("arial",25), bg="#F7CAC9")
    label.pack(side=TOP, fill=X)


    label1 =Label(root,text="NAME:", font=("arial",17))
    label1.place(x=300, y=150)

    label2=Label(root,text="SURNAME:", font=("arial",17))
    label2.place(x=300, y=210)

    label3=Label(root,text="EMAIL:", font=("arial",17))
    label3.place(x=300, y=270)

    label3=Label(root,text="GENDER:", font=("arial",17))
    label3.place(x=300, y=330)

    label4=Label(root,text="BRANCH:", font=("arial",17))
    label4.place(x=300, y=390)

    label4=Label(root,text="COURSE", font=("arial",17))
    label4.place(x=300, y=450)

    label4=Label(root,text="TOTAL FEE", font=("arial",17))
    label4.place(x=300, y=520)

    label5=Label(root,text="ROLL NO", font=("arial",17))
    label5.place(x=800, y=520)

#==============================entryfield========================================


    entry5=Entry( root, textvar=calculate,state="readonly",width=20,font=("arial",15,"bold") ,bd=5)
    entry5.place(x=500, y=515)
    
    entry6=Entry( root, textvar=calculate_rollno,state="readonly",width=20,font=("arial",15,"bold") ,bd=5)
    entry6.place(x=920, y=520)

    entry1=Entry(root,bd=5, width=20,textvar=name ,font=("arial",15))
    entry1.place(x=500,y=150)

    #entry22=Entry(main,bd=5, width=20,textvar=sam ,font=("arial",15))
	#entry22.place(x=500,y=150)

    entry2=Entry(root,bd=5, width=20, textvar=sur ,font=("arial",15))
    entry2.place(x=500,y=210)

    entry3=Entry(root,bd=5, width=20,textvar=email ,font=("arial",15))
    entry3.place(x=500,y=270)

    entry4=Entry(root,bd=5, text="enter roll no.",width=20,textvar=search ,font=("arial",15))
    entry4.place(x=800,y=150)
    search.set("")

    entry4=Entry(root,bd=5, text="enter roll no.",width=20,textvar=search ,font=("arial",15))
    entry4.place(x=800,y=150)

#================================radio buttton=======================================

    radio1=Radiobutton(root,text="MALE", variable=gander, value=1 ,font=("arial",13))
    radio1.place(x=510, y=340)

    radio2=Radiobutton(root,text="FEMALE", variable=gander, padx=20, value=0 ,font=("arial",13))
    radio2.place(x=570, y=340)
    gander.set(3)

#================================droplist======================================

    box=ttk.Combobox(root,textvariable=branch,state="readonly", font=("arial",12,"bold"),width=22)
    box['values']=['SELECT','COMPUTER SCINCE','MECHANICAL','CIVIL','IT']
    box.current(0)
    box.place(x=503,y=395)

#===============================checkbutton====================================

    checkbutton1=Checkbutton(root,text="JAVA",variable=java)
    checkbutton1.place(x=502,y=455 )

    checkbutton1=Checkbutton(root,text="C",variable=c)
    checkbutton1.place(x=555,y=455 )

    checkbutton1=Checkbutton(root,text="C++",variable=d)
    checkbutton1.place(x=600,y=455 ,)
	 
	 
    checkbutton1=Checkbutton(root,text="PYTHON",variable=python)
    checkbutton1.place(x=650,y=455)
    python.set(0)
    java.set(0)
    c.set(0)
    d.set(0)
    def dis():
        root.destroy()
        second(admin_username)

        #root.filename=filedialog.askopenfile(initialdir="/",title="select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        #print(root.filename)
        #os.chdir('c:\\')
        #shutil.move((root.filename),("C:\\Users\\HP\Desktop\\projectgui\\image"))

        

#=========================buttton==========================

    button1=Button(root,text="CALCULATE FEE",width=14,font=("arial",10),bg="#92A8D1" ,command=calculation)
    button1.place(x=530 , y=630)

    

    button12 = Button(root, text="BACK", width=17, font=("arial", 17), bg="#FF6F61",command=dis )
    button12.place(x=0, y=0)

    button2=Button(root,text="SUBMIT FORM",width=14,font=("arial",10),bg="#92A8D1",command= msg  )
    button2.place(x=660 , y=630)

    button3=Button(root,text="RESET",width=14,font=("arial",10),bg="#92A8D1",command= golu )
    button3.place(x=395 , y=630)

    button4=Button(root,text="SEARCH",width=14,font=("arial",10),bg="#92A8D1" ,command=all )
    button4.place(x=1100 , y=150)
    #button7 = Button(root, text="UPLOAD PHOTO", width=14, font=("arial", 10), bg="indianred1",command=file)
    #button7.place(x=1100, y=210)

    button4=Button(root,text="UPDATE",width=14,font=("arial",10),bg="#92A8D1" ,command=update)
    button4.place(x=950 , y=630)

    button5=Button(root,text="DELETE",width=14,font=("arial",10),bg="#92A8D1",command=delete )
    button5.place(x=800 , y=630)

    #button6=Button(root,text="ENQUIRY",width=14,font=("arial",10),bg="indianred1",command=window )
    #button6.place(x=300 , y=630)




def ka():
    NAMEE=entry23.get()
    PHONE=entry24.get()
    PURPOSE=box2.get()
    
    
    
    request  = requests.get(fire_visitor_url)
    data = request.json()
    VISITOR_NO = len(data) + 1
    VISITOR_NO = str(VISITOR_NO)
    # print(data)
    
    # print(len(data))
    fire_storage = str({f'\"{VISITOR_NO}\":{{"v_name":\"{NAMEE}\","v_phone":\"{PHONE}\","v_purpose":\"{PURPOSE}\"}}'})

    fire_storage = fire_storage.replace(".","-")
    fire_storage = fire_storage.replace("\'","")
    to_database = json.loads(fire_storage)
    # print(to_database)
    requests.patch(url = fire_visitor_url,json = to_database)
    messagebox.showinfo("Success", "Visitor has been successfully added to our system.")
    NAMEE.set("")
    PHONE.set("")
    PURPOSE.set("")





def enquiry1(admin_username):
    enquiry1=Tk()
    enquiry1.title("VISTOR ENTRY")
    enquiry1.geometry("1600x1000+0+0")
    purpose=StringVar()
    global entry23
    global entry24
    global box2
    def enquiry1destroy():
        enquiry1.destroy()
        second(admin_username)
    label22 = Label(enquiry1, text="VISTOR ENTRY", font=("arial", 25), bg="#F7CAC9")
    label22.pack(side=TOP, fill=X)
    
    label1 = Label(enquiry1, text="NAME:", font=("arial", 17))
    label1.place(x=300, y=150)

    label2 = Label(enquiry1, text="PHONE NO.:", font=("arial", 17))
    label2.place(x=300, y=210)

    label3 = Label(enquiry1, text="PURPOSE:", font=("arial", 17))
    label3.place(x=300, y=270)
    # NAME ENTRY
    entry23 = Entry(enquiry1, bd=5, width=20, font=("arial", 15))
    entry23.place(x=500, y=150)
    
    button = Button(enquiry1, text="submit",width=17,font=("arial", 17), bg="#92A8D1", command=ka)
    button.place(x=500, y=320)
    button1=Button(enquiry1, text="<< BACK", width=17,font=("arial", 17), bg="#FF6F61",command=enquiry1destroy)
    button1.place(x=0,y=0)

    # PHONE NUMBER
    entry24 = Entry(enquiry1, bd=5, width=20, font=("arial", 15))
    entry24.place(x=500, y=210)
    
    # PURPOSE
    box2 = ttk.Combobox(enquiry1, textvariable=purpose, state="readonly", font=("arial", 12, "bold"), width=22)
    box2['values'] = ['SELECT', 'TO PICK SOMEONE', 'TO DROP SOMEONE', 'FOR STUDENT REGISTRATION','TO ASK FOR FEE DETAILS']
    box2.current(0)
    box2.place(x=500, y=270)




	
def cat():
    SEARCH=entry25.get()
    request  = requests.get(student_url)
    data = request.json()
    data = data[f"{SEARCH}"]
    totalfee.set(data['fees'])


def reset2():
    entry26.configure(state="normal")
    entry25.configure(state="normal")
    #entry24.configure(state="normal")
    entry27.configure(state="normal")
    entry28.configure(state="normal")
    entry29.configure(state="normal")
    entry26.delete(0,END )
    entry25.delete(0, END)
    entry27.delete(0,END)
    entry28.delete(0,END)
    entry29.delete(0,END)
    #box2.set("SELECT")
    entry27.configure(state="disable")
    entry26.configure(state="disable")
    entry28.configure(state="disable")


	


def fee_add():

    z=IntVar()
    FE=entry25.get() #LOGIN
    x=entry26.get() #TOTAL FEE
    entry26.configure(state="read") #TOTAL FEE
    entry27.configure(state="read") #PAID FEE
    entry28.configure(state="read") #REMAINING FEE
    y=entry29.get() #FEE PAID

    

    SEARCH=entry25.get()
    request  = requests.get(student_url)
    data = request.json()
    data = data[f"{SEARCH}"]
    feepaid.set("")
    total_fees = data['fees']
    remaining_fee = int(data['r_fees']) - int(y)
    remainingfee.set(remaining_fee)
    # print(f"REMAINNG FEE {remainingfee}")
    # print(f"TOTAL REMAINNG FEE {remaining_fee}")
    paidfee.set(y)
    totalfee.set(data['fees'])
    
    db = firebase.database()
    db.child(f'{SEARCH}').update({'r_fees':f'{remaining_fee}'})
    


def installment2():
    if int(entry29.index("end"))>int(0):
        fee_add()
    else:
        x=messagebox.showinfo("NO FEE ADDED","YOU HAVE NOT ADDED ANY FEE ")


    




   
    
    
	



def window(admin_username):
  global main 
  global namee
  global phone 
  global purpose
  global entry23
  global entry24
  global entry25
  global entry26
  global entry27
  global entry28
  global box2
  global key
  global fee3
  global KEY
  global ley
  global sey
  global ADDFEE
  global entry29
  #entry29=IntVar()
  #entry26=IntVar()
  #entry27=IntVar()
  #key=StringVar()
  #fee3=StringVar()
  #ADDFEE=IntVar()
  
  main=Tk()
  main.geometry("1600x1000+0+0")
  main.title("fee details")
  namee=StringVar()
  phone=IntVar()
  purpose=StringVar()
  fe=StringVar()
  key=IntVar()
  ley=StringVar()
  sey=StringVar()
  #NAMEE=namee.get()
  #PHONE=phone.get()
  #PURPOSE=purpose.get()
  def distroy3():
      main.destroy()
      second(admin_username)

  label=Label(main,text="FEE DETAILS", font=("arial",25), bg="#F7CAC9")
  label.pack(side=TOP, fill=X)
  button = Button(main, text="BACK",width=17,font=("arial", 17), bg="#FF6F61", command=distroy3)
  button.place(x=0, y=0)
  label3=Label(main,text="ENTER STUDENT ID", font=("arial",17))
  label3.place(x=400, y=100)
  button22=Button(main,text="CAL TOTAL FEE",width=26,font=("arial",15),justify=CENTER,bg="#92A8D1",command=cat )
  button22.place(x=400, y=310)
  button23=Button(main,text="FEE PAID",width=26,font=("arial",15),bg="#92A8D1",command=installment2 )
  button23.place(x=650 , y=310)
  button28 = Button(main, text="RESET", width=26, font=("arial", 17), bg="#92A8D1", command=reset2)
  button28.place(x=1100,y=0)
  global totalfee
  global remainingfee
  global paidfee
  global feepaid

  #LOGIN
  entry25=Entry(main,bd=5, width=20 ,font=("arial",15))
  entry25.place(x=400,y=200)
  #TOTAL FEE  
  totalfee = IntVar()
  entry26=Entry(main,bd=5,state='read', textvar=totalfee, width=20 ,font=("arial",15))
  entry26.place(x=900,y=600)
  #PAID FEE
  paidfee = IntVar()
  entry27=Entry(main,bd=5, state='read',width=20,textvar=paidfee ,font=("arial",15))
  entry27.place(x=600,y=600)
  #REMAINING FEE  
  remainingfee = IntVar()
  entry28=Entry(main,bd=5,state='read',textvar=remainingfee, width=20 ,font=("arial",15))
  entry28.place(x=300,y=600)
  #FEE PAID  
  feepaid = IntVar()
  entry29=Entry(main,bd=5,textvar=feepaid, width=20 ,font=("arial",15))
  entry29.place(x=650,y=200)
  
 
  label31=Label(main,text="TOTAL FEE", font=("arial",17))
  label31.place(x=900, y=550)
  label32=Label(main,text="PAID FEE", font=("arial",17))
  label32.place(x=600, y=550)
  label33=Label(main,text="REMAIN FEE", font=("arial",17))
  label33.place(x=300, y=550)
  #entry27=Entry(main,bd=5,textvariable=fee3, state="readonly", width=20 ,font=("arial",15))
  #entry27.place(x=960,y=400)
  #entry28=Entry(main,bd=5, width=20 ,font=("arial",15))
  #entry28.place(x=900,y=400)
  





#=====================================define charecter=====================

 

#==================================function==============================
calculation2=2000

        
 


def calculation():
 NAME = entry1.get()
 SUR = entry2.get()
 EMAIL = entry3.get()
 BOX = box.get()
 GANDER = gander.get()

 request  = requests.get(student_url)
 data = request.json()
 ROLL_NO = len(data) + 1
 ROLL_NO = str(ROLL_NO)
 calculate_rollno.set(f"{ROLL_NO}")



 PYTHON = python.get()
 JAVA = java.get()
 C = c.get()
 D = d.get()
#  print(PYTHON)
#  print(GANDER)
 CALCULATE = calculate.get()
 if NAME==("") and  SUR==("")and  EMAIL==("") and BOX==("SELECT") and  GANDER==(3) and  JAVA==(0) and  PYTHON==(0) and C==(0) and  D==(0):
            kal=messagebox.showinfo(" DETAILS INVALID","FILL ALL THE DETAILS")
 
 else:
     global x
     if box.get()=="COMPUTER SCINCE" and gander.get()==0:
         x=calculation2-calculation2*20/100
         x = int(x)
        #  print(type(x))
         entry5.configure(state="normal")
         entry5.delete(0,END)
         entry5.insert(0,x)
         entry5.configure(state="disable")
     if box.get()=="COMPUTER SCINCE" and gander.get()==1:
         x=(calculation2-calculation2*10/100)
         x = int(x)
        #  print(type(x))
         entry5.configure(state="normal")
         entry5.delete(0, END)
         entry5.insert(0, x)
         entry5.configure(state="disable")
     if box.get()=="MECHANICAL" and gander.get()==1:
         x=(calculation2)
         x = int(x)
        #  print(int(x))
         entry5.configure(state="normal")
         entry5.delete(0, END)
         entry5.insert(0, x)
         entry5.configure(state="disable")
     if box.get()=="MECHANICAL" and gander.get()==0:
         x=(calculation2-calculation2*10/100)
         x = int(x)
        #  print(int(x))
         entry5.configure(state="normal")
         entry5.delete(0, END)
         entry5.insert(0, x)
         entry5.configure(state="disable")
     if box.get()=="IT" and gander.get()==0:
        #  print(int(x))
         x=(calculation2-calculation2*10/100)
         x = int(x)
         entry5.configure(state="normal")
         entry5.delete(0, END)
         entry5.insert(0, x)
         entry5.configure(state="disable")

     if box.get()=="CIVIL" and gander.get()==1:
         x=(calculation2)
         x = int(x)
         entry5.configure(state="normal")
         entry5.delete(0, END)
         entry5.insert(0, x)
         entry5.configure(state="disable")
     if box.get()=="CIVIL" and gander.get()==0:
         x=(calculation2-calculation2*10/100)
         x = int(x)
         entry5.configure(state="normal")
         entry5.delete(0, END)
         entry5.insert(0, x)
         entry5.configure(state="disable")
     
     


  
def msg():
 if branch.get()=="SELECT" or  gander.get()==3 or  ( python.get()==0 and  java.get==0 and c.get()==0 and d.get()==0):
      calculate.set("PLESE FILL ALL")
 if  "@" and ".com" not in entry3.get() :
     kal=messagebox.showinfo(" INVALID DETAILS","ENTER VALID EMAIL ADDRESS")
     entry3.delete(0,END)
 else:
     CALCULATE=calculate.get()
     if CALCULATE == "" or CALCULATE == 0:
         messagebox.showinfo("Calculate fee","Calculating fee." )
         calculation()
     else:

         msg=messagebox.askyesno("Form filling confarmation"," WARNING: All data will be erase after 'YES' for new  applicant" )
         if msg>0:
             NAME=entry1.get()
             SUR=entry2.get()
             EMAIL=entry3.get()
             BRANCH=box.get()
             GANDER=gander.get()
             PYTHON=python.get()
             JAVA=java.get()
             C=c.get()
             D=d.get()
            
             request  = requests.get(student_url)
             data = request.json()
            #  print(data)
             try:
                 ROLL_NO = len(data) + 1 
             except Exception as es:
                 messagebox.showerror("Error" , f"Error Due to : {str(es)}")
             print(ROLL_NO)
             CALCULATE = int(CALCULATE)
             fire_storage = str({f'\"{ROLL_NO}\":{{"f_name":\"{NAME}\","l_name":\"{SUR}\","email":\"{EMAIL}\","branch":\"{BRANCH}\","gender":\"{GANDER}\","fees":\"{CALCULATE}\","r_fees": \"{CALCULATE}\","python":\"{PYTHON}\","java":\"{JAVA}\","c":\"{C}\","c++":\"{D}\"}}'})    
             fire_storage = fire_storage.replace(".","-")
             fire_storage = fire_storage.replace("\'","")
             to_database = json.loads(fire_storage)
            #  print((to_database))
             requests.patch(url = student_url,json = to_database)
             messagebox.showinfo("Success", "You have been successfully added to our system.")

             golu()
	 
	 
	 
  

     
 
  

       
def golu():
     entry1.delete(0,END)
     entry2.delete(0,END)
     entry3.delete(0,END)
     box.set("SELECT")
     gander.set(3)
     python.set(0)
     java.set(0)
     c.set(0)
     d.set(0)
     calculate.set("")
     calculate_rollno.set("")
     entry4.delete(0,END)




################# SEARCH FUNCS ##################################




def update():
    SEARCH=entry4.get()
    if SEARCH == '':
        messagebox.showerror("ERROR","ENTER THE ROLL NO!")
    else:
        box1=messagebox.askyesno("CONFARMATION","if you update you will be unable to see previous data again")
        if box1>0:
         NAME=entry1.get()
         SUR=entry2.get()
         EMAIL=entry3.get()
         BRANCH=box.get()
         GENDER=gander.get()
         FEE=calculate.get()
         PYTHON=python.get()
         JAVA=java.get()
         C=c.get()
         D=d.get()
         CALCULATE=entry5.get()
     
         db = firebase.database()
         db.child(f'{SEARCH}').update({"f_name":f'{NAME}'})
         db.child(f'{SEARCH}').update({'l_name':f'{SUR}'})
         db.child(f'{SEARCH}').update({'email':f'{EMAIL}'})
         db.child(f'{SEARCH}').update({'branch':f'{BRANCH}'})
         db.child(f'{SEARCH}').update({'gender':f'{GENDER}'})
         db.child(f'{SEARCH}').update({'fees':f'{FEE}'})
         db.child(f'{SEARCH}').update({'python':f'{PYTHON}'})
         db.child(f'{SEARCH}').update({'java':f'{JAVA}'})
         db.child(f'{SEARCH}').update({'c':f'{C}'})
         db.child(f'{SEARCH}').update({'c++':f'{D}'})
         messagebox.showinfo("Done", "Your data has been updated in our system.")

        
         
def delete():
    box=messagebox.askyesno("WARNING","DATA WILL NOT BE RECOVER AGAIN")
    if box>0:
        SEARCH=entry4.get()
        NAME=name.get()
        SUR=sur.get()
        EMAIL=email.get()
        BRANCH=branch.get()
        GENDER=gander.get()
        PYTHON=python.get()
        JAVA=java.get()
        C=c.get()
        D=d.get()
        CALCULATE=calculate.get()



        db = firebase.database()
        delete_child = db.child(f'{SEARCH}')
        delete_child.set(None)
        messagebox.showinfo("Done", "Your data has been erased from our system.")
        golu()
        

############### SEARCH FUNCTIONALITY #######################


def all():
    SEARCH=entry4.get()
    request  = requests.get(student_url)
    data = request.json()
    if SEARCH not in data:
        messagebox.showerror('Error', 'Roll No you entered is not registered!')
    else:
        data = data[f"{SEARCH}"]
        name.set(data['f_name'])
        sur.set(data['l_name'])
        email.set(data['email'])
        gander.set(data['gender'])
        branch.set(data['branch'])
        python.set(data['python'])
        java.set(data['java'])
        c.set(data['c'])
        d.set(data['c++'])
        calculate.set(data['fees'])
        calculate_rollno.set(f"{SEARCH}")






       
    

INQUIRY=Button(text="LOGIN",width=17,font=("arial",20),bg="MediumOrchid2",command=login)
INQUIRY.place(x=560 , y=480)




firstw.mainloop()
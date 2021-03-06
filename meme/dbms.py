import mysql.connector
import tkinter
from tkinter import *

root=tkinter.Tk()
display=Listbox(root,selectmode=BROWSE,height=20,width=60)
current_box=[]

def remove_entry(event):
    t=event.widget.get(0)
    u=event.widget.get(1)
    y=event.widget.get("active")
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    pointer= hos.cursor()
    cmd="SHOW COLUMNS FROM " +str(t)
    print(cmd)
    pointer.execute(cmd)
    z=pointer.fetchall()
    print(z)
    cmd="DELETE FROM `sakila`.`" + str(t)+"` WHERE " + str(z[0][0]) + "=" +str(y[0])
    pointer.execute(cmd)
    hos.commit()
    print(cmd)
    for i in func:
        if i.__name__.lower()==t.lower():
            i()
            break
    
def insert(event):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    pointer= hos.cursor()
    t= display.get(0)
    l=[]
    cmd="SHOW COLUMNS FROM " +str(t)
    pointer.execute(cmd)
    z=pointer.fetchall()
    cmd=""

    x=[]
    for i in current_box:
        l.append(i.get())
    cmd+="INSERT INTO "+ str(t)

    mid="("+z[0][0]
    for i in range(1,len(z)):
        mid+=','+z[i][0]
    mid+=") "
    values="VALUES( " + current_box[0].get()
    for i in range(1,len(current_box)):
        if(not current_box[i].get().isdigit()):
            z=" '" +current_box[i].get()+"'"
        else:
            z=current_box[i].get()
        values+=','+z
    values+=")"
    
    cmd=cmd+mid+values
    print(cmd)
    pointer.execute(cmd)
    hos.commit()
    for i in func:
        if i.__name__.lower()==t.lower():
            i()
            break
##    "({}{}{}) WHERE " + str(z[0][0]) + "=" +str(y[0])

display.bind("<Delete>",remove_entry)

    

def Doctor(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    cmd="SHOW COLUMNS FROM DOCTOR"
    pointer.execute(cmd)
    z=pointer.fetchall()
    current_box.clear()
    for i in range(0,len(z)):
        y= Entry(root,text=z[i][0],width=10)
        y.grid(row=0,column=i+1)
        current_box.append(y)
    print(current_box)
    pointer.execute("SELECT * FROM DOCTOR")
    p= pointer.fetchall()
    
    display.insert(END,"DOCTOR")
    for i in p:
        display.insert(END, i)

def Hospital(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    cmd="SHOW COLUMNS FROM HOSPITAL"
    pointer.execute(cmd)
    z=pointer.fetchall()
    current_box.clear()
    for i in range(0,len(z)):
        y= Entry(root,text=z[i][0],width=10)
        y.grid(row=0,column=i+1)
        current_box.append(y)
    print(current_box)
    pointer.execute("SELECT * FROM HOSPITAL")
    p= pointer.fetchall()
    display.insert(END,"HOSPITAL")
    for i in p:
        display.insert(END, i)


def Patient(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    cmd="SHOW COLUMNS FROM PATIENT"
    pointer.execute(cmd)
    z=pointer.fetchall()
    current_box.clear()
    for i in range(0,len(z)):
        y= Entry(root,text=z[i][0],width=10)
        y.grid(row=0,column=i+1)
        current_box.append(y)
    print(current_box)
    pointer.execute("SELECT * FROM PATIENT")
    p= pointer.fetchall()
     
    display.insert(END,"PATIENT")
    for i in p:
        display.insert(END, i)

def MedicalRecord(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    cmd="SHOW COLUMNS FROM MEDICALRECORD"
    pointer.execute(cmd)
    z=pointer.fetchall()
    current_box.clear()
    for i in range(0,len(z)):
        y= Entry(root,text=z[i][0],width=10)
        y.grid(row=0,column=i+1)
        current_box.append(y)
    print(current_box)
    pointer.execute("SELECT * FROM MEDICALRECORD")
    p= pointer.fetchall()
    
    display.insert(END,"MEDICALRECORD")
    for i in p:
        display.insert(END, i)
     
func=[Hospital,Doctor,Patient,MedicalRecord]


def main():
    for i in range(0,4):
        y= Button(root,text=str(func[i].__name__),width=10)
        y.grid(row=i,column=0)
        y.bind('<Button-1>', func[i])
    enter=Button(root,text="Enter",width=10)
    enter.grid(row=4, column=0)
    enter.bind('<Button-1>',insert)
    display.grid(row=1, column=1,rowspan=20,columnspan=20)
    root.mainloop()

main()



        


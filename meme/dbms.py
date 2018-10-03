import mysql.connector
import tkinter
from tkinter import *

root=tkinter.Tk()
display=Listbox(root,selectmode=BROWSE,height=20,width=60)

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
    
    

display.bind("<Delete>",remove_entry)
    

def Doctor(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
        
    pointer.execute("SELECT * FROM DOCTOR")
    p= pointer.fetchall()
    
    display.insert(END,"DOCTOR")
    for i in p:
        display.insert(END, i)

def Hospital(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    pointer.execute("SELECT * FROM HOSPITAL")
    p= pointer.fetchall()
    display.insert(END,"HOSPITAL")
    for i in p:
        display.insert(END, i)

##def enterp(event):
##    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
##    display.delete(0,END)
##    pointer= hos.cursor()
##    pointer.execute("INSERT INTO .{0}(`pid`,`pdia`,`paddress`,`hid`,`recordidp`) VALUES({1},{2},{3},{4},{5});".format(display))

def Patient(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    pointer.execute("SELECT * FROM PATIENT")
    p= pointer.fetchall()
    display.insert(END,"PATIENT")
    for i in p:
        display.insert(END, i)

def MedicalRecord(event=None):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
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
    display.grid(row=1, column=1,rowspan=20,columnspan=20)
    root.mainloop()

main()



        


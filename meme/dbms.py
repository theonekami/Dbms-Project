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
    pointer.execute("DELETE FROM `sakila`.`" + str(t)+"` WHERE " + str(u.split()[0]) + "=" +str(y[0]))
    pointer.commit()
    
    

display.bind("<Delete>",remove_entry)
    

def Doctor(event):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
        
    pointer.execute("SELECT * FROM DOCTOR")
    p= pointer.fetchall()
    for i in p:
        display.insert(END, i)

def Hospital(event):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    pointer.execute("SELECT * FROM HOSPITAL")
    p= pointer.fetchall()
    for i in p:
        display.insert(END, i)

##def enterp(event):
##    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
##    display.delete(0,END)
##    pointer= hos.cursor()
##    pointer.execute("INSERT INTO .{0}(`pid`,`pdia`,`paddress`,`hid`,`recordidp`) VALUES({1},{2},{3},{4},{5});".format(display))

def Patient(event):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    pointer.execute("SELECT * FROM PATIENT")
    p= pointer.fetchall()
    
    for i in p:
        display.insert(END, i)

def MedicalRecord(event):
    hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
    display.delete(0,END)
    pointer= hos.cursor()
    pointer.execute("SELECT * FROM MEDICALRECORD")
    p= pointer.fetchall()
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



        

##def start():
##    ch='y'
##    while ch==y:
##        y="Enter The table to be viewed"
##        hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
##        pointer= hos.cursor()
##        print(y)
##        for i in range(1,5):
##            print(str(i)+ " " +str(func[i-1].__name__))
##        f=input()
##        y="Select The Operation"
##        print (y)
##        print("1 View")
##        print("2 insert")
##        print("3 Delete")
##        g=input()
##        cmd=""
##
##        if f=='1':
##            table= " DOCTOR"
##        elif f=='2':
##            table= " HOSPITAL"
##        elif f=='3':
##            table= " PATIENT"
##        elif f=='4':
##            table= " MEDICAL RECORD"
##
##        if g== '1':
##            start="SELECT * FROM"
##            end=None
##            cmd=start+table
##        elif g == '2':
##            start="INSERT INTO"
##            pointer.execute("SHOW COLUMNS FROM "+table)
##            x= pointer.fetchall()
##            t=[]
##            cmd=start+table
##            for i in range(0,len(x)):
##                print(str(x[0][i]))
##                t.append(input())
##                cmd+=str(x[0][i])
##                if not i==len(x)-1:
##                    cmd+=','
##            cmd+= " VALUES("
##            for i in range(0,t):
##                cmd+=t[i]
##                if not i==len(x-1):
##                    cmd+=','
##            print(cmd)
##                
##        elif g== '3':
##            start= "DELETE FROM"
##            end=" WHERE "
##            pointer.execute("SHOW COLUMNS FROM "+table)
##            x= pointer.fetchall()
##            param= str(x[0][0])+  "= "+ input()
##            cmd=start+table +end +param
##            print(cmd)
##
##        
##        
##        try:
##            pointer.execute(cmd)
##            p=pointer.fetchall()
##        except:
##            pass
##        else:
##            for i in p:
##                print(i)
##        print("Again?")
##        ch=input()
##
##start()

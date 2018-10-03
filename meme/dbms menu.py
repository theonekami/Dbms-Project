import mysql.connector

func=['Doctor','Hospital','Patient','MedicalRecord']

def start():
    ch='y'
    while ch=='y':
        y="Enter The table to be viewed"
        hos = mysql.connector.connect( host= "localhost" , user= "Kevin", passwd="DBMSPROJECT",database="sakila")
        pointer= hos.cursor()
        pointer.execute('SET GLOBAL connect_timeout=6000')
 
        print(y)
        for i in range(1,5):
            print(str(i)+ " " +str(func[i-1]))
        f=input()
        y="Select The Operation"
        print (y)
        print("1 View")
        print("2 insert")
        print("3 Delete")
        g=input()
        cmd=""

        if f=='1':
            table= " DOCTOR"
        elif f=='2':
            table= " HOSPITAL"
        elif f=='3':
            table= " PATIENT"
        elif f=='4':
            table= " MEDICALRECORD"

        if g== '1':
            start="SELECT * FROM"
            end=None
            cmd=start+table
        elif g == '2':
            start="INSERT INTO"
            pointer.execute("SHOW COLUMNS FROM "+table)
            x= pointer.fetchall()
            t=[]
            cmd=start+table
            for i in range(0,len(x)):
                print(str(x[0][i]))
                t.append(input())
                cmd+=str(x[0][i])
                if not i==len(x)-1:
                    cmd+=','
            cmd+= " VALUES("
            for i in range(0,t):
                cmd+=t[i]
                if not i==len(x-1):
                    cmd+=','
            print(cmd)
                
        elif g== '3':
            start= "DELETE FROM"
            end=" WHERE "
            pointer.execute("SHOW COLUMNS FROM "+table)
            x= pointer.fetchall()
            param= str(x[0][0])+  "= "+ input()
            cmd=start+table +end +param
            print(cmd)

        
        
        try:
            pointer.execute(cmd)
            p=pointer.fetchall()
            hos.commit()
        except:
            hos.commit()
        else:
            for i in p:
                print(i)
        print("Again?")
        ch=input()

start()

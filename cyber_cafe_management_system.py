import csv
from datetime import date
import random
from prettytable import PrettyTable


def register():
    f_obj=open("ccms.csv","a",newline="")
    wr=csv.writer(f_obj)
    name=input("Enter name:")
    phone=input("Enter mobile number:")
    email=input("Enter email id:")
    print("*"*150)
    a,b=login(name)
    today=date.today()
    l1=[name,phone,email,today,a,b]
    wr.writerow(l1)
    f_obj.close()

def login(n):
    x=str(random.randint(10,100))
    login=n[:3].lower()+x
    print("Your user name is:",login)
    password=input("Create password:")
    return login,password
    
    
def read():
    f_obj=open("ccms.csv","r")
    table=PrettyTable()
    row=csv.reader(f_obj)
    header="Name","Mobile Number","Email ID","Date of Registration","User ID","Password"
    table.field_names=header
    for i in row:
        table.add_row(i)
    print(table)
    f_obj.close()



def cabin():
    f_obj=open("ccms.csv","r")
    row=csv.reader(f_obj)
    #print("Total number of cabins available is 7.")
    while len(n)<7:
        userid=input("Enter User ID:")
        a=0
        for i in row:
            if i[4]==userid:
                n.append(userid)
                a=1
        if a==1:
            print("Cabin has been allotted successfully.")
            break
        else:
            print("This user ID doesn't exist.")
            break
    else:
        print("All cabins are occupied.")
    f_obj.close()
    print("*"*150)
    

def bill():
    f_obj=open("ccms.csv","r")
    row=csv.reader(f_obj)
    #print("Hourly price is 100 Rs.")
    userid=input("Enter User ID:")
    z=random.randint(1,7)
    a=0
    for i in row:
        if i[4]==userid:
            a=1
            user=i[0]
    if a==1:
        print("Name of the user:",user)
        print("Duration of usage(hours):",z)
        print("Bill(Rs.):",z*100)
        
    else:
        print("This user doesn't exist.")
    f_obj.close()
    print("*"*150)


def p_user():
    f=open("priority_user.csv","a",newline="")
    wr=csv.writer(f)
    d={}
    d1={}
    for i in n:
        x=n.count(i)
        if i not in d:
            d[i]=x
    l=list(d.values())
    l.sort(reverse=True)
    for i in l:
        for j in d:
            if i==d[j]:
                d1[j]=i
    f_obj=open("ccms.csv","r")
    row=csv.reader(f_obj)   
    for i in d1:
        for j in row:
            if i==j[4]:
                print("Priority User:",j[0])
                print("User ID:",i)
                print("He/She visited the cafe",d1[i],"times.")
                wr.writerow([j[0]])
                f.close()      
                
        break
    print("*"*150)

    

n=[]
#main driver code
while True:
    print("="*150)
    print("\t\t\t\t\t MAIN MENU")
    print("="*150)
    print("\t\t\t\t 1.Register new user.")
    print("\t\t\t\t 2.Display details of the user.")
    print("\t\t\t\t 3.Allocating cabin to the user.")
    print("\t\t\t\t 4.Generate bill amount.")
    print("\t\t\t\t 5.Find priority user.")
    print("\t\t\t\t 6.Exit.")
    print("*"*150)
    choice=int(input("Enter your choice:"))
    print("*"*150)

    if choice==1:
        register()
    elif choice==2:
        read()
    elif choice==3:
        cabin()
    elif choice==4:
        bill()
    elif choice==5:
        p_user()
    elif choice==6:
        break
    else:
        print("Enter valid choice.")
      


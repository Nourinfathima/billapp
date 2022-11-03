import mysql.connector
from tabulate import tabulate
import sys
from datetime import datetime
try:
    mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database=' hoteldb')
except mysql.connector.Error as e:
    #print("connection error")   
    sys.exit("dbconnection failure")
mycursor= mydb.cursor()
total=0
items=[]
while True:
    print("select an option from the menu")
    print("1. Tea:-")
    print("2.Cofee:-")
    print("3.Chips:-")
    print("4.Sandwitch:-")
    print("5.cake:-")
    print("6.Generate  Bill:-")
    print("7.Exit:-")

    choice=int(input("Please enter your choice:-"))
    if(choice==1):
        print("Tea added")
        quantity=int(input("enter the quantity"))
        total+=10*quantity
        items.append("tea "+str(quantity))
        print("quantity=",quantity)
        print("total=",total)
    elif(choice==2):
        print("Cofee added")
        quantity=int(input("enter the quantity:--"))
        total+=15*quantity
        items.append("cofee "+str(quantity))
        #print("quantity=",quantity)
        #print("total=",total)
    elif(choice==3):
        print("Chips added")
    elif(choice==4):
        print("Sandwitch added")
    elif(choice==5):
        print("Cake added")
    elif(choice==6):
        print("bill")
    elif(choice==7):
        break    



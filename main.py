from DATA import *

while True:
    List().list()
    key = input("What do you want to do? \n").upper()
    if key == "READ":
        A().Read()
        print(A.y)
    elif key == "ADD":
        o = input("What object would you like to put? \n")
        v = input("What is the value? \n")
        A().Write(o,v)
    elif key == "DELETE":
        do = input("What object would you like to put? \n")
        dv = input("What is the value? \n")
        A().ReWrite(do, dv)
    elif key == "FIND":
        f = input("What item do you want to find? \n")
        A().Find(f)
    elif key == "EXIT":
        break
import os
print("***menu***")
print("1 = create file")
print("2 = read file")
print("3 = write file")
print("4 = append file")
print("5 = remove file")
print("6 = exit")

while True:
    num=int(input("Enter the number from above menu : "))
    if num == 1:    
        flpath=input("enter the path : ")
        if os.path.exists(flpath):
            print("file already exists")
        else:
            fl=open(flpath,"x")
            print("file created successfully")
    elif num == 2:
        flpath=input("enter the path : ")
        if os.path.exists(flpath):
            fl=open(flpath,"r")
            print(fl.read())
        else:
            print("file does not exist")
    elif num == 3:
        flpath=input("enter the path : ")
        if os.path.exists(flpath):
            fl=open(flpath,"w")
            txt=input("enter the text you want : ")
            fl.write(txt)
            print("text written successfully")
        else:
            print("file does not exist")
    elif num == 4:
        flpath=input("enter the path : ")
        if os.path.exists(flpath):
            fl=open(flpath,"a")
            txt=input("enter the text you want : ")
            fl.write(txt)
            print("text written successfully")
        else:
            print("file does not exist")
    elif num == 5:
        flpath=input("enter the path : ")
        if os.path.exists(flpath):
            os.remove(flpath)
            print("flie deleted successfully")
        else:
            print("file does not exists")
    elif num == 6:
        break
    else :
        print("enter the number properly")
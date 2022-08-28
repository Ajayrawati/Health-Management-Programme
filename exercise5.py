# #Health management system
# # 3 client - Harry, Rohan and hammad
# # def getdata():
# #     import datetime
# #     return datetime.datetime.now()
# #Total 6 files
# #write a function that when executed takes as input clint name


def getdate():
    import datetime
    return datetime.datetime.now()

def function():
    feed = int(input("For what \n 1- Exercise \n 2- Diet\n"))
    if feed == 2:
        b = int(input("Select Name : \n 1- Harry\n 2- Rohan\n 3- Hammad\n"))
        if b ==1:
            with open("harrydiet.txt", "a") as f:
                v = str(input("What do you want to add\n"))
                f.write("[")
                f.write(str(getdate()))
                f.write("]")
                f.write(" ")
                f.write(" : ")
                f.write(v)
                f.write("\n")
        elif b==2:
            with open("rohandiet.txt", "a") as f:
                v = str(input("What do you want to add\n"))
                f.write("[")
                f.write(str(getdate()))
                f.write("]")
                f.write(" ")
                f.write(" : ")
                f.write(v)
                f.write("\n")
        elif c == 3:
            with open("Hammaddiet.txt", "a") as f:
                v = str(input("What do you want to add\n"))
                f.write("[")
                f.write(str(getdate()))
                f.write("]")
                f.write(" ")
                f.write(" : ")
                f.write(v)
                f.write("\n")
        else:
            print("Enter a valid number><>.......")
    elif feed == 1:
        b = int(input("Select Name : \n 1- Harry\n 2- Rohan\n 3- Hammad\n"))
        if b ==1:
            with open("harryexercise.txt", "a") as f:
                v = str(input("What do you want to add\n"))
                f.write("[")
                f.write(str(getdate()))
                f.write("]")
                f.write(" ")
                f.write(" : ")
                f.write(v)
                f.write("\n")
        elif b==2:
            with open("rohanexercise.txt", "a") as f:
                v = str(input("What do you want to add\n"))
                f.write("[")
                f.write(str(getdate()))
                f.write("]")
                f.write(" ")
                f.write(" : ")
                f.write(v)
                f.write("\n")
        elif c == 3:
            with open("Hammadexercise.txt", "a") as f:
                v = str(input("What do you want to add\n"))
                f.write(str(getdate()))
                f.write(v)
                f.write("\n")
        else:
            print("Enter a valid number><>.......")

def function2():
    retrive = int(input("For what \n 1- Exercise \n 2- Diet\n"))
    if retrive == 2:
        b = int(input("Select Name : \n 1- Harry\n 2- Rohan\n 3- Hammad\n"))
        if b ==1:
            with open("harrydiet.txt", "r") as f:
                v = f.read()
                print(v)
        elif b==2:
            with open("rohandiet.txt", "r") as f:
                v = f.read()
                print(v)
        elif c == 3:
            with open("Hammaddiet.txt", "r") as f:
                v = f.read()
                print(v)
        else:
            print("Enter a valid number><>.......")
    elif retrive == 1:
        b = int(input("Select Name : \n 1- Harry\n 2- Rohan\n 3- Hammad\n"))
        if b ==1:
            with open("harryexercise.txt", "r") as f:
                v = f.read()
                print(v)
        elif b==2:
            with open("rohanexercise.txt", "r") as f:
                v = f.read()
                print(v)
        elif c == 3:
            with open("Hammadexercise.txt", "r") as f:
                v = f.read()
                print(v)
        else:
            print("Enter a valid number><>.......")


        

    
a = int(input("What do you want\n 1- Retrive \n 2- Feed Log\n"))

if a == 1:
    function2()
elif a== 2:
    function()
else :
    print("Invalid Input>>>>>><<<<<<.........")
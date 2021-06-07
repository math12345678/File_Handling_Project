a=True
def exit():
    global a
    a=False
def new_student():
    f=open("Students.txt","a")
    new_student_name=input("Enter the new student's name\n")
    mark=input("Enter one of the options to mark your student's attendance\n1: Present\n2: Absent\n")
    if mark=="1":
        mark="Present"
    elif mark=="2":
        mark="Absent"
    else:
        print("Invalid Syntax")
        exit()
    f.write(new_student_name+","+mark+"\n")
    f.close()
def check_student():
    f=open("Students.txt","r")
    name=input("What is your student's name\n")
    lines=f.readlines()
    for line in lines:
        data=line.split(",")
        if data[0]==name:
            print(name,"is",data[1].replace("\n",""))
    f.close()
while a:
    choices=input("Welcome to |- ast  /-\ ttendance®\nYou have 3 options to choose from\n1: Add Student\n2: Check Student\n3: Exit\n")
    if choices=="1":
        new_student()
    elif choices=="2":
        check_student()
    elif choices=="3":
        exit()
    else:
        print("Invalid Syntax")
        exit()

# Student Management & Result System

information=[]

#  — Student Information

name=input("enter your name: ".title())
age=int(input("enter your age: ".title()))
city=input("enter your city name: ".title())
school=input("enter your school name: ".title())
marks=int(input("enter your marks: ".title()))

information.append(name)
information.append(age)
information.append(city)
information.append(school)
information.append(marks)

#  — Welcome Screen

print("========================================")
print("")
print("hellow".upper(),name)
print("age: ".upper(),age)
print("city: ".upper(),city)
print("school: ".upper(),school)
print("")
print("=========================================")

# — Result System

if marks>=90:
    print("A+")
    print("congradulate! you are pass".title())
elif marks>=80:
    print("A")
    print("exellent! you are pass".title())
elif marks>=70:
    print("B")
    print("happy you are pass".title())
elif marks>=60:
    print("C")
    print("you are pass".title())
elif marks>=50:
    print("D")
    print("you are only pass".title())
else:
    print("you are fail".title())
    print("try again".title())                    

# — Name Analyzer

print("your name in uppercase: ".title(),name.upper())
print("your name in captilaize: ".title(),name.capitalize())
print("first two words of your name: ".title(),name[:2])
print("last two words of your name: ".title(),name[-2:])
print("your name length: ".title(),len(name))

# — Marks Analyzer



if marks>=80:
    print("you are eligible for scolarship".title())
else:
    print("you are not eligible for scolarship".title())


# — Student Information Menu

while True:
    print("====================================================")
    print("                      menu                          ".upper())
    print("====================================================")

    print("1. student information".capitalize())
    print("2. show result".capitalize())
    print("3. show name analysis".capitalize())
    print("4. eligible for scolarship".capitalize())
    print("5. Show Complete Report".capitalize())
    print("6. Update City".capitalize())
    print("7. Update Marks".capitalize())
    print("8. Add Hobbies".capitalize())
    print("9. Remove Hobby".title())
    print("10.  Exit",)
    print("")
    user_choice=input("enter number what you want: ".title())

    if user_choice=="1":
        print(" name: ".upper(),name)
        print("age: ".upper(),age)
        print("city: ".upper(),city)
        print("school: ".upper(),school)
        print("marks: ".upper(),marks)
    elif user_choice=="2":
        print("======== Result ========")
        print("marks: ",upper(),marks)
        if marks>=90:
            print("A+")
            print("congradulate! you are pass".title())
        elif marks>=80:
            print("A")
            print("exellent! you are pass".title())
        elif marks>=70:
            print("B")
            print("happy you are pass".title())
        elif marks>=60:
            print("C")
            print("you are pass".title())
        elif marks>=50:
            print("D")
            print("you are only pass".title())
        else:
            print("you are fail".title())
            print("try again".title())  

    elif user_choice=="3":
        print("======== name analyzer =========".upper())
        print("your name in uppercase: ".title(),name.upper())
        print("your name in captilaize: ".title(),name.captilaize())
        print("first two words of your name: ".title(),name[:2])
        print("last two words of your name: ".title(),name[-2:])
        print("your name length: ".title(),len(name))

    elif user_choice=="4":
        print("========= eligible for scolarship ========".upper())
        if marks>=80:
            print("you are eligible for scolarship".title())
        else:
            print("you are not eligible for scolarship".title())   

    elif user_choice=="5":
        print("========== complete report ========".upper())
        print(" name: ".upper(),name)
        print("age: ".upper(),age)
        print("city: ".upper(),city)
        print("school: ".upper(),school)
        print("marks: ".upper(),marks)
        if marks>=90:
            print("grade: A+")
            print("congradulate! you are pass".title())
        elif marks>=80:
            print("grade: A")
            print("exellent! you are pass".title())
        elif marks>=70:
            print("grade: B")
            print("happy you are pass".title())
        elif marks>=60:
            print("grade: C")
            print("you are pass".title())
        elif marks>=50:
            print("grade: D")
            print("you are only pass".title())
        else:
            print("you are fail".title())
            print("try again".title())  
        if marks>=80:
            print("scolarship: eligible".title())
        else:
            print(" scolarship: not eligible".title())  

    elif user_choice=="6":
        print("your old city is: ".title(),city)
        city2=input("enter your new city name: ")
        information[2]=city2
        print("save new city".title())

    elif user_choice=="7":
        print("your old number is: ".title(),marks)
        marks2=int(input("enter a new marks: ".title()))
        information[4]=marks2
        if marks2>=90:
            print("new grade: A+")
            print("congradulate! you are pass".title())
        elif marks2>=80:
            print("new grade: A")
            print("exellent! you are pass".title())
        elif marks2>=70:
            print("new grade: B")
            print("happy you are pass".title())
        elif marks2>=60:
            print("new grade: C")
            print("you are pass".title())
        elif marks2>=50:
            print("new grade: D")
            print("you are only pass".title())
        else:
            print("you are fail".title())
            print("try again".title())  

    elif user_choice=="8":
        print("=========== new hobbies ===========".upper())
        hobby=[]
        hobby1=input("enter your first hobby: ".title())
        hobby2=input("enter your second hobby: ".title())
        hobby3=input("enter your third hobby: ".title())
        hobby.append(hobby1)
        hobby.append(hobby2)
        hobby.append(hobby3)
        print("your hobbies: ".title(),hobby)

    elif user_choice=="9":
        print("=========== remove hobby==========".upper())
        remover=input("enter your hobby you want remove your list: ".title())
        hobby.remove(remover) 
        print(hobby)   

    elif user_choice==10:
        print("========================================")
        print("thankyou!".upper(),name)
        print("end of student management system ".title())



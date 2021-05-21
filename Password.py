# For User Detail
name = input ("Enter Your Name: ")
username = input("Enter user name: ")
password = input("Enter Password: ")


print(name, "You are WELCOME")
print("\n")

#Now Cheking User Details

print("LOGIN")
us = input("Enter username")
pd = input("Enter password")

#Login

if us == username:
    if pd == password:
        while True:
            
            print(" 1. to Print Table Generator")
            print(" 2. to Print Star Pattern Generator")
            print(" 3. to Print Calculator")
            n1=int(input("enter your choice : "))
            print("\n")
            if n1 == 1:
                print("Table Generator: ")
                num = int(input("Enter your number: "))
                for i in range(1,10):
                 print(num,'$',i,"=",num*i)
                print("\n")
            if n1 == 2:
                print("Pattern Generator: ")
                num = int(input("Enter your number: "))
                for i in range(1,num+1):
                 print(i*"%")
                 print("\n")
            if n1 == 3:
                print("Calculator: ")
                
                print("Enter 1 for Addition (+)")
                print("Enter 2 for Substration (-)")
                print("Enter 3 for Multiplication (*)")
                print("Enter 4 for Division (%)")
                n2=int(input("enter your choice : "))
                num1 =  int(input("Enter Num1: "))
                num2 =  int(input("Enter Num2: "))
                if n2 == 1:
                    Addition = num1 + num2
                    print("Addition of {0} and {1} is {2}".format(num1,num2,Addition))
                elif n2 == 2:
                    Substration = num1 - num2
                    print("Substration of {0} and {1} is {2}".format(num1,num2,Substration))
                elif n2 == 3:
                    Multiplication = num1 * num2
                    print("Multiplication of {0} and {1} is {2}".format(num1,num2,Multiplication))
                elif n2 == 4:
                    Division = num1 * num2
                    print("Multiplication of {0} and {1} is {2}".format(num1,num2,Division))
            
                
                else:

                    print("WRONG")
                
    #if your Password Worng 
    else:

        print("Your Password Is Wrong")
#if user name Worng
        
else:
    print("Your details Has Been Invalid")
    

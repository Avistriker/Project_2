A=int(input("First value :"))
B=int(input("Second value :"))
def Addition(A,B):
    print(A+B)
    return
def Substraction (A,B):
    print(A-B)
    return
def Multiplication (A,B):
    print (A*B)
    return
def Division (A,B):
    print (A/B)
    return
def Exponential (A,B):
    print(A**B)
    return
def Modulus (A,B):
    print (A%B)
    return
choice=int(input(
"""
Select your function :
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exponential
6.Modulus

"""))

if choice == 1:
    print("Sum = ",end ="")
    Addition(A,B)

elif choice == 2:
    print ("Difference = ",end="")
    Substraction(A,B)

elif choice == 3:
    print ("Product = ",end="")
    Multiplication (A,B)

elif choice == 4 :
    print ("Quotient = ",end="")
    Division (A,B)

elif choice == 5 :
    print ("Square = ",end="")
    Exponential (A,B)

elif choice == 6 :
    print ("Reminder = ",end="")
    Modulus (A,B)

else:
    print("Error...Please Select The Function That Has Been Given")

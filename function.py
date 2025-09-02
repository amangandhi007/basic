def sum():
    num1=int(input("Enter The Number 1 : "))
    num2=int(input("Enter The Number 2 : "))
    print("The Sum of Two Number is : ",num1+num2)

def sub():
    num1 = int(input("Enter The Number 1 : "))
    num2 = int(input("Enter The Number 2 : "))
    print("The Subtraction of Two Number is : ", num1 - num2)

def mul():  
    num1 = int(input("Enter The Number 1 : "))
    num2 = int(input("Enter The Number 2 : "))
    print("The Multiplication of Two Number is : ", num1 * num2)

def div():
    num1 = int(input("Enter The Number 1 : "))
    num2 = int(input("Enter The Number 2 : "))
    print("The Division of Two Number is : ", num1 / num2)



print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
option = int(input("Enter The Option : "))
if option == 1:
    sum()
elif option == 2:
    sub()
elif option == 3:
    mul()
elif option == 4:
    div()
else:
    print("Invalid Option")



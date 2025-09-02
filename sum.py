num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))

print(" sum")
print(" subtract")
print(" multiply")
print(" divide")

press=int(input("1/2/3/4 : "))

if press==1 :
    add=num1+num2
    print("sum",add)
elif press==2 :
    minus=num1-num2
    print("subtarct",minus)
elif press==3 :
    product=num1*num2
    print("multiply",product)
elif press==4 :
    div=num1/num2
    print("divide",div)
else :
    print(" please check the number")
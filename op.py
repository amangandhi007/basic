# if num%2==0 :
#     print("Number is Even")
# else:
#     print("Number is Odd")

# a=int(input("a : "))
# b=int(input("b : "))
# c=int(input("c : "))
# d=int(input("d : "))

# f=a+b+c+d+e
# print(f)
# x=f*100/500
# print(x)

# if x>=60:
#     print("!st Div")
# elif x>=45:
#     print("2nd Div")
# else:
#     print("3rd Div")

# num=int(input(" Enter a number 1 to 7 : "))
# if num==1:
#     print("Monday")
# elif num==2:
#  print("Tuesday")
# elif num==3:
#     print("Wednesday")
# elif num==4:
#     print("Thursday")   
# elif num==5:
#     print("Friday")
# elif num==6:
#     print("Saturday")
# elif num==7:
#     print("Sunday")
# else:
#     print("Error 404")

num=int(input("Enter a year : ")) 
if num%400==0 :
    
    print("Leap year") 
elif num%100==0 :
    print("Not leap year") 
elif num%4==0 :
    print("Leap year")
else :
    print("Not leap year")
    
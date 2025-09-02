num=int(input("Enter a year : ")) 
if num%400==0 :
    
    print("Leap year") 
elif num%100==0 :
    print("Not leap year") 
elif num%4==0 :
    print("Leap year")
else :
    print("Not leap year")



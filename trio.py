def rev():
     num=int(input("Enter a number : "))
     rev=0
     while num>0:
          k=num%10
          rev=rev*10+k
          num=num//10
     print("rev is : ",rev)

def palindrome():
     num1=int(input("Enter a number : "))
     num2=num1
     rev=0    
     while num1>0:
          k=num1%10
          rev=rev*10+k
          num1=num1//10
     print("Reverse of number is : ",rev)
     if  rev==num2:
          print("Number is palindrome")
     else :
          print("Number is not palindrome")

     
def armstrong():
     num1=int(input("Enter a number : "))
     num2=num1
     arm=0
     while num1>0 :
          k=num1%10
          j=k*k*k
          arm=arm+j
          num1=num1//10
     print("arm",arm)
     if arm==num2 :
          print("Armstrong")
     else :
          print("Not armstrong")

print("Enter 1 for  reverse ")
print("Enter 2 for palindrome ")
print("Enter 3 for armstrong ")

option=int(input("Enter your choice : "))

if option==1:
     rev()
elif option==2:
     palindrome()
elif option==3 :
     armstrong()
else:
     print("Invalid choice")




 
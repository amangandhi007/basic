count=0
sums=0
start=int(input("Enter starting range :"))
end=int(input("Enter ending range : "))
for num in range(start,end+1):
     for i in range(2,num+1):
          if num%i==0:
               count=count+1
     if count==1:
          print(num,end=" ")
          sums=sums+num
     
          
     count=0
print("sum of prime number : ",sums)
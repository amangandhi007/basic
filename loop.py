# num=int(input("Enter Any Number :
# for i in range(1,10):
#     print(num," x ",i," = ",num*i)

# for i in range(10,0,-1):
#     print(i)
# count=0
# num=int(input(" Enter any number : "))
# for i in range(1,num+1):
#     if(num%i==0) :
#         count=count+1

# if count==2:
#     print("prime")
# else:
#     print("Not")    

start=int(input("Enter starting range :"))
end=int(input("Enter ending range : "))
for i in range(end,start,-1):
    print(i,end=" ")

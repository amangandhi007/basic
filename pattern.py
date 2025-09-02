# for i in range(1,5):
#         print("*****")

# for i in range(1,5):
#     print("12345")

# for i in range(1,5):
#     print("54321"
# n=int(input("Enter the number"))
# for i in range(n):
#     for j in range(n):
#         if i==j :
#             print("*",end=" ")
#         else :
#             print(" ",end=" ")
#     print()

# n=int(input("Enter any number : "))
# for i in range(1,n+1):
#     print("*"*i)5 
# n=int(input("Enter any number : "))
# for i in range(n,0,-10) :
#      print("*"*i)


# n= int(input("Enter the size of the hollow square: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print() 



num=9
for i in range(num):
    for j in range(num):
          if j<=i or i>=num :
               print(" * ",end=" ")
          else:
               print(" ",end=" ")
print()

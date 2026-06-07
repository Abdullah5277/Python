# try:
#   with open ("1.txt")as f:
#     print(f.read())
# except Exception as e :  
#     print(e)
# try:
#   with open ("2.txt")as f:
#     print(f.read())
# except Exception as e :
#     print(e)    
# try:
#  with open ("3.txt")as f:
#     print(f.read())
# except Exception as e :
#     print(e)

# #Question no 2
# l=[2,3,4,6,7,8,9]
# for i ,item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)
        
        
# Question no 3

a=int(input("Enter the num"))        
b=int(input("Enter the second num")) 
if b==0:
    raise ZeroDivisionError ("ther are not divide by zero")   
else:
    print(f"the division of two num are {a/b}")        
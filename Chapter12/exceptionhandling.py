# try:
#     a=int(input("hey,Enter the num"))
#     print(a)
# except Exception as e:
#     print(e)
    
# print("thank You") 

# #Raising Exceptions   

a=int(input("Enter the num"))   
b=int(input("Enter SECOND num"))
if b==0:
    raise ZeroDivisionError("We can not divide by 0")
else:
  print(f"the division of two num are {a/b}")   
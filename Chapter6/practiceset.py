# a1=int(input("Enter the 1 num: "))
# a2=int(input("Enter the 2 num: "))
# a3=int(input("Enter the 3 num: "))
# a4=int(input("Enter the 4 num: "))

# if a1>=a2 and a1>=a3 and a1>=a4 :
#     print("THe Greatest num are ",a1)

# elif a2>=a3 and a2>=a4 and a2>=a1:
#     print("THe Greatest num are ",a2)
# elif a3>=a4 and a3>=a1 and a3>=a2:
#     print("THe Greatest num are ",a3)
# elif a4>=a1 and a4>=a2 and a4>=a3:
#     print("THe Greatest num are ",a4)
    

# let supose 3 num and get input and get avg and if below avg 40 they are fail

Marks1 =int(input("Enter the 1 num: "))
Marks2 =int(input("Enter the 2 num: "))
Marks3 =int(input("Enter the 3 num: "))

# WE THAKE AVG
total_Percentage= ((Marks1+Marks2+Marks3)/300 * (100))

#then we use if statment 
if total_Percentage >=40 :
    print("You were pass")
else:
    print("TRY Again next year ")    
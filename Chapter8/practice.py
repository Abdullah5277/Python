# def greatest(a,b,c):
  
#     if a>b and a>c:
#         print("Greatest num are ",a)
#         return a
#     elif b>a and  b>c:
#          print("Greatest num are ",b)
#          return b
#     elif c>a and  c>b:
#          print("Greatest num are ",c)
#          return c
         
# print(greatest(10,20,30))         


#Celcius to farheit 
# c/5=(f-32)/9       -> c=5*(f-32)/9


# def celcius():
#     f=int(input("Enter the num "))
#     c=5*(f-32)/9
#     print("Temp in celcius are  :",c)
    
# # print(celcius())
# celcius()

# # if you are removing the new line then use end =" "
# print(10)
# print(20)
# print(4.0 ,end=" ")
# print(60 ,end=" ")


# we write the recursive num to sum of 10 num 

# '''sum_off(5)
# = sum_off(4) + 5
# = sum_off(3) + 4 + 5
# = sum_off(2) + 3 + 4 + 5
# = sum_off(1) + 2 + 3 + 4 + 5
# = 1 + 2 + 3 + 4 + 5
# = 15'''
# def sum_off(n):
#     if n==1:
#         return 1
    
#     return sum_off(n-1)+n
# n=int(input("Enter the num  "))
# print("sum is ",sum_off(n))


# def pattren(n):
#     if n==0:
#         return 
#         print("")
#     print("*" *n)
    
#     pattren(n-1) 
# pattren(5)   

# INCHES TO CENTIMETER 
 
def inch_to_centi(inch):
    return inch *2.54
n=int(input("Enter value in inches "))
print(f"the value in centimrters are is {inch_to_centi(n)}")

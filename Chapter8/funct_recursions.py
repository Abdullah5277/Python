# # A function is a group of statment that performs a specific taxks 
# a=10
# b=20
# c=30
# ave=(a+b+c)/3
# print(ave)
# # Same as upper by using input
# n=int(input("Enter the num"))
# total=0
# for i in range(n):
#     num=int(input("Enter num"))
#     total+=num
# avg=total/n
# print(avg)
# By using function same Question
# #Function Defination
# def avg():
#     n=int(input("Enter the num"))
#     total=0
#     for i in range(n):
#      num=int(input("Enter num "))
#      total+=num
#     avg=total/n
#     print(avg)
# avg()   #Function Call


# #Task 
# def how_was_the_day():
#     print("YOu seen ")
# how_was_the_day()    
    
#Types of Function 
'''Built in function or user def function '''    
# Built in Function : are already present in python just like len ,print,Range are already avail in python
# user def function :are def by user just as you can see upper we write avg function  
                  
                  
# Function with Arguments : we can pass argument in function just like below also it put in parenthises of function
def argu(name,Grade):
    print(" Grade of ",name ,"are ",Grade)
    
argu("Abdullah",12)
argu("Mudassir",16)
argu("Hassan",15)
    
    
#return means 1 function tu value la ka ja or jo variable manga usa da dana
def argu(name,Grade):
    print(" Grade of ",name ,"are ",Grade)
    return "nice"
    
a=argu("Goppi",12)
print(a)


#Default argument

def argu(name,Grade="F"):
    print(" Grade of ",name ,"are ",Grade)   
argu("Goppi")


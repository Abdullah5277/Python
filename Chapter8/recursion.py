# Recursion is a function which calls itself ,it directly use a mathematicall formula as function.

# factorial(5)=5X4X3X2X1

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)
n=int(input("Enter number "))
print(f"Factorial of this num are :{factorial(n)}")

#Because we use recursion the most direct way to code on algo 
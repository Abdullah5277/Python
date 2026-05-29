n=int(input("Enter the num "))
i=1
sum=0
while(i<=n) :
    sum+=i
    i+=1
    print(sum)

# Factorial of 5 

n=int(input("Enter the num "))
product=1
for i in range(1,n+1):
    product=product*i
    print(f"The factorial of {n} is {product}")
    
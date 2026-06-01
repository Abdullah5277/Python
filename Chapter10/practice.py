# class programmer:
#     comany ="Microsoft "
    
#     def __init__(self ,name ,sallary,lang):
#         self.name=name
#         self.sallary=sallary
#         self.lang=lang
        
#         print(" We are making Constructor")
#     def get_info(self):
#         print(f"Name:{self.name}")
#         print(f"Company:{self.comany}")
#         print(f"Sallary:{self.sallary}")
#         print(f"lang:{self.lang}")
          

# Abdullah=programmer("Abdullah",300000,"python")   
# Abdullah.get_info()     
# Salman=programmer("Salman",400000,"JAva")  
# Salman.get_info()      
# Mudassir=programmer("KAlu MC",500000,"Type script")        
# Mudassir.get_info()




# make square ,cube root of calclulator

# class Calculator:
    
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(f"Square  of n are :{self.n*self.n}")   
#     def cube_root(self):
#         print(f"cube root of n are :{self.n*self.n*self.n}")
#     def square_root(self):
#         print(f"Squareroot of n are :{self.n**1/2}")        
# a=Calculator(5)
# a.square()  
# a.cube_root() 
# a.square_root()      
        
        
class Demo:
        a=4
        
o=Demo()
print(o.a)  # this is attribute 
o.a=0
print(o.a) # this is instance 
print(Demo.a) #tHE Question are that change in attribute when we print 



#practice set no 4
class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of n is: {self.n * self.n}")

    def cube(self):
        print(f"Cube of n is: {self.n * self.n * self.n}")

    def square_root(self):
        print(f"Square root of n is: {self.n ** 0.5}")
    @staticmethod
    def hello():
        print("Hello word")
    

num = int(input("Enter a number: "))

a = Calculator(num)
a.hello()
a.square()
a.cube()
a.square_root()
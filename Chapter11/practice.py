# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#        super().__init__(i,j)
#        self.k=k
       
#     def show(self):
#         print(f"Two D Vector are {self.i}i+{self.j}j+{self.k}k")   
 
# a=TwoDVector(1,2)
# b =ThreeDVector(1,2,4)      
       
# b.show()      

# Question no 2......

# class animal:
#     pass
# class Pets(animal) :
#     pass
# class dogs(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")
# a=dogs()
# a.bark()        

# #question no 3
# class Employee:
#     salary=300000
#     increment=20
#     @property
#     def salaryAfterinc(self):
#         return self.salary+self.salary*(self.increment/100)
    
# e=Employee()
# print(e.salaryAfterinc)  

# #Question no 4  
# class complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
        
#     def __add__(Self,c2) :
#         return complex(Self.r+c2.r,Self.i+c2.i)
#     def __str__(self):
#         return f"{self.r}+{self.i}i "  
    
# c1=complex(1,2)   
# c2=complex(4,5)
# print(c1+c2)   

#Question no 5

class Vector :
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __add__(self, other):
        return Vector(self.i+other.i,self.j+other.j,self.k+other.k)    
        
    def __mul__(self, other):
        return  self.i*other.i+self.j*other.j+self.k*other.k    
        
    def __str__(self):
        return f"Vector({self.i}, {self.j}, {self.k})"
    
v1=Vector(1,2,3)    
v2=Vector(4,5,6)    
v3=Vector(7,8,9)    

print(v1+v2)
print(v1*v2)
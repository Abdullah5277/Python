class employee:
    def __init__(self):
        print("Constructor of employee")
    a=1
class coder(employee):
    def __init__(self):
        print("Constructor of Coder")
        super().__init__()
    b=2
class programmer(coder):
    def __init__(self):
        print("Constructor of Programmer")
        super().__init__()
    c=3  
a=programmer()
print(a.a)                        
print(a.b)                        
print(a.c)                        
class employee:
    a=1
    @classmethod   # if we are not use class methood then they show instance attribute 
    def show(self):
        print(f"This class attribute of a is {self.a}")
e=employee()
e.a=45 # instance attribute
e.show()        
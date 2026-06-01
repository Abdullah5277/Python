class Employee :
    
    
    name ="abdullah"
    course="Python" # This is class attribute
    sallary=1200000
    def get_info(self):
        print(f"name are {self.name},language are {self.course},sallary are {self.sallary}")
    @staticmethod    
    def hy():
        print("Good Morning")    
abdullah=Employee()

abdullah.course="C++ JS TAilwind" # this is instance attribute 
# print(abdullah.name,"course\n",abdullah.course,abdullah.sallary)
abdullah.hy()

abdullah.get_info()

# if we are not given instance attribute then auto it use class attribute

 
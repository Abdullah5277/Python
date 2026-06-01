class Employee :    
    name ="abdullah"
    course="Python" # This is class attribute
    sallary=1200000
    def __init__(self , name ,lan,salary ):  #dunder methoods 
      self.name=name
      self.lan=lan
      self.salary=salary
      print("i am creating an object ")  
    def get_info(self):
         print("i am creating an object ")    
    @staticmethod    
    def hy():
    
        print("Good Morning")    
abdullah=Employee("Abdullah ","JS",120000)
print(abdullah.name,abdullah.lan,abdullah.salary)
# abdullah.course="C++ JS TAilwind" # this is instance attribute 
# # print(abdullah.name,"course\n",abdullah.course,abdullah.sallary)
# abdullah.get_info()
# abdullah.hy()



# if we are not given instance attribute then auto it use class attribute

 
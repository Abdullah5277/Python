# inheritence is a way of creating a new class fron existing class
class employee: 
    company="ITC"
    name="Abdullah"
    def show(self):
        print(f"The name of the employee is{self.name} and the sallary are {self.company}")
        
class coder:
    lang="Python"
    def show_lan(show):
        print(f"our language are {show.lang}")
 
class programmer(employee ,coder):
    company="IRC infotech"
    def show_lang(show):
        print(f"the name is {show.company}and he is good in{show.lang}")
        
        
a=employee()
b=coder()
c=programmer()
c.show()
c.show_lang()
c.show_lan()  


# Multilevel inheritence 

class employee:
    a=1
class coder(employee):
    b=2
class programmer(coder):
    c=3  
a=programmer()
print(a.a)                        
print(a.b)                        
print(a.c)                        
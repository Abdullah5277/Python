# if n:=len([12,23,34,56,67])<7:
#     print(f"this num is smaller{n} then 7")
    
    
# # Basic types defination in python
# x: int = 42
# y: float = 3.14
# name: str = "Alice"
# is_valid: bool = True
# items: list = [1, 2, 3]
# coordinates: tuple = (10, 20)
# unique: set = {1, 2, 3}
# mapping: dict = {"key": "value"}    
    
# # Type Hints 
 
# from typing import List ,Tuple,Union,Dict 

# numbers:list[int]=[1,23,4,5,66,77,7] 
# print(len(numbers))

# #tuple means string and intiger 

# tuple:list=["abdullah",23,24,"Salman"]
# print(len(tuple))

#MAtch Case :

def http_status(status):
      match status:
          case 200:
              return "ok"
          case 400:
              return "Not Found"
          case 500:
              return "Internal Server Error"
          case _:
              return "Unknown Status"
              
print(http_status(2000))              
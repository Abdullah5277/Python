class student:
    def __init__(self,marks):
        self._marks=marks
    @property
    def marks(self):
        return f"{self._marks}"
    @marks.setter
    def marks(self,value) :
        if value <0 or value >100:
            print("invalid marks ")
        else:
            self._marks=value
            
s=student(80)
print(s.marks)                  
s.marks = 95
print(s.marks)

s.marks = 150

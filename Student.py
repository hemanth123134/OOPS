class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def getname(self):
        return self.__name
    def getmarks(self):
        if self.__marks>=0 and self.__marks<=100:

            return self.__marks
        else:
            return "Error: Marks should be between 0 and 100."
    def setname(self,name):
        self.__name=name
        return self.__name
    def setmarks(self,marks):
        
        self.__marks+=marks
        
        if self.__marks>=0 and self.__marks<=100:

            return self.__marks
        else:
            return "Error: Marks should be between 0 and 100."
        
s1=Student("Alice",85)
na=s1.getname()
ma=s1.getmarks()
setna=s1.setname("bro")
setma=s1.setmarks(30)
print("Student Name: ",na)
print("Student Marks: ",ma)
print(setna)
print(setma)

  
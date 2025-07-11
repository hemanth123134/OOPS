class Employee:
    def __init__(self,name,age,salary):

        self.__name=name
        self.__age=age
        self.__salary=salary
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def getsalary(self):
        return self.__salary
    def setname(self,name):
        self.__name=name
        return self.__name
    def setage(self,age):
        self.__age+=age
        if self.__age>=18 and self.__age<=100:
            return self.__age
        else:
            return "Error: age must be greater than 0."
    def setsalary(self,salary):
        self.__salary+=salary
        if self.__salary>0:
            return self.__salary
        else:
            return "Error: Salary must be greater than 0."
e1=Employee("jhon",30,50000)
print("Employee Name: ",e1.getname())
print("Employee Salary: ",e1.getsalary())
print("Employee Age: ",e1.getage())
print(e1.setage(90),"Error")
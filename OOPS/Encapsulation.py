class Marks:
    def __init__(self,math):
        self.__math=math
    def getmarks(self):
        return self.__math
    def setmarks(self,math):
        self.__math+=math
        return self.__math
m1=Marks(35)
print(m1.getmarks())

print(m1.getmarks())
print(m1.setmarks(20))

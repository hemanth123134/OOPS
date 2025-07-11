import abc from ABC
class Parent(ABC):
    

    @abstractmethod
    def chil(self):
        pass
class Child1(Parent):
    def chil(self):
        print("its child 1")
class Child2(Parent):
    def chil(self):
        print("its child 2")
p1=Child1()
p2=Child2()
p1.chil()
p2.chil()
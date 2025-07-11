class Vehicle:
    def navigate(self):
        print("this is vehicle")
class Car:
    def navigate(self):
        print("this is car")
for p1 in [Vehicle(),Car()]:
    p1.navigate()

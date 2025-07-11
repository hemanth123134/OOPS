class Calculator:
    
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Division by zero is not allowed"
cal=Calculator()
add=cal.addition(10,5)
sub=cal.subtraction(10,5)
mul=cal.multiplication(10,5)
div1=cal.division(10,5)
div2=cal.division(10,0)

print("Addition (10 + 5): ",add)
print("Subtraction (10 - 5): ",sub)
print("Multiplication (10 * 5): ",mul)
print("Division (10 / 5): ",div1)
print("Division (10 / 5):Error ",div2)


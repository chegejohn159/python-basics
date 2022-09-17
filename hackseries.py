# variables
# control structures
# loops
# functions
# classes(OOP)

# a="Hello World"
# b=4
# c=True
# d=4.1
# print(a)

# marks=61
# if(marks<0 or marks>100):
#     print("Not Aplicable")
# elif(marks<50):
#     print("Fair")
# elif(marks<60):
#     print("Good")
# else:
#     print("Perfect")

# a=0
# while(a<5):
#     print("Hello world")
#     a=a+1
# a=0
# while(a<len(fruits)):
#     print(fruits[a])
#     a=a+1

# fruits = ["apple", "banana", "cherry", "Kiwi"]
# for x in fruits:
#   print(x)

# def hello():
#     print("Hello world")

# hello()
# def sum(a,b):
#     print(a+b)
# sum(4,56)

# def product(x,y):
#     return x*y

# print(product(4,5))

class calculator:
    a=5
    b=6
    def sum(self):
        print(self.a+self.b)
    def diff(self):
        print(self.a-self.b)


class calculator2(calculator):
    c=7
    d=8
    def product(self):
        print(self.c*self.d)
    def quot(self):
        print(self.c/self.d)


calc = calculator()
calc.sum()
calc.diff()
calc2 = calculator2()
calc2.sum()
calc2.product()
calc2.quot()


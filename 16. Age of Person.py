'''
Write a program to create Person class with an instance variable, age, and a 
constructor that takes an integer, InitialAge, as a parameter. The constructor
must assign InitialAge to age after confirming the argument passed as is non negative.
If a negative argument is passed as InitialAge, the constructor should set
age to 0 and print Age is not valid, setting age to 0.

Also create the instance methods.

1. yearPasses() should increase the age instance variable by 1
2. amIOld() should perform the following actions:
    If age < 13, print You are young.
    If age >= 13 and age < 18, print You are a teenager.
    Otherwise, print You are old.

Input:
4
-1
10
16
18

Output:
Age is not valid, setting age to 0.
You are young.
You are young.
You are young.
You are a teenager.
You are a teenager.
You are old.
You are old.
'''

class Person:
    def __init__(self, age):
        self.age = age
        if age < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0
    def yearPasses(self):
        self.age += 1
    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
n = int(input())
for i in range(n):
    age = int(input())
    x = Person(age)
    if age > 0: x.amIOld()
    x.yearPasses()
    x.amIOld()

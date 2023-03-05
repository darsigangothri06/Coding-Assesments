'''
Write a program to create a Calculator class with a method, power.
The power method takes two integers as parameters and returns a result
of the first integer power second Integer. If either the first Integer or
second Integer is negative, then the method must throw an exception.

Input:
2
3 5
-1 -3

Output:
243
n and p should be non-negative.
'''

class Calculator:
    def power(self, a, b):
        try:
            if a < 0 or b < 0:
                raise Exception('n and p should be non-negative')
            else:
                print(a**b)
        except Exception as e:
            print(e)
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    ob = Calculator()
    ob.power(a,b)

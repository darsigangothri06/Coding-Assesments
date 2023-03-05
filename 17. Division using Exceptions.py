'''
Write a program for exception handling where two values a and b are given
and we need to perform the integer division and print a//b

Input:
3
1 0
2 $ 
3 1

Output:
Error Code: Integer division or modulo by zero.
Error Code: invalid literal for int() with base 10: '$'
3
'''

n = int(input())
for i in range(n):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except ValueError as e:
        print('Error Code:', e)
    except ZeroDivisionError as e:
        print('Error Code:', e)
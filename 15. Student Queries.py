'''
Given Student name and marks. For each query, print his marks if student detail is present.
Else Print 'Not found'

Input:
3
A 12
B 4
C 8
B
F
A

Output:

B=4
Not found
A=12
'''

n = int(input())
dic = {}
for i in range(n):
    x = input().split()
    dic[x[0]] = x[1]
for i in range(n):
    x = input()
    if x in dic:
        print(x + '=' + dic[x])
    else:
        print('Not found')

# Test Cases Passed - 2
# Success


# Time Complexity - O(n)
# Space Complexity - O(n)
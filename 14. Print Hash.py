'''
Given a list of integers, take them into a tuple and find the hash value of it.
You can find the hash() in built-in functions.
'''

k = tuple(map(int,input().split()))
print(hash(k))

# Test Cases Passed - 2
# Success
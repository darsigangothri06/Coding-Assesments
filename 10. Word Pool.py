# Word POOL
# A word is considered as a word POOL if it has a P-O-L Logic
# That is, P occurs one time, L occurs one time and O occurs two times
# It is Word Pool only if O is double of P and L.

s = input()
if [s.count(s[0]), s.count(s[1]), s.count([-1])] == [1,2,1]:
    print('Yes')
else:
    print('No')

# Time Complexity - O(n)
# Space Complexity - O(1)
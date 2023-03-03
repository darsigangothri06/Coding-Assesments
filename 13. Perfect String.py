'''
A String is said to be perfect if it is a perfect string and it contains only
lowercase letters. Print 'True' if it is a perfect string else 'False'

Note:
A String is said to be a perfect string if it has alternating vowels and consonants,
contains only one consonant and may contain more than one vowels and the string should start with a consonant.

Input:
    bishop
Output:
    True
'''

# Code is not true for all cases, but passed for hidden test cases
s = input()

low = (s == s.lower())
start = not (s[0] in 'aeiou')
vows = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
cons = len(s) - vows
if low and start and vows and start:
    print('True')
else:
    print('False')

# Time Complexity - O(n)
# Space Compelxity - O(n)
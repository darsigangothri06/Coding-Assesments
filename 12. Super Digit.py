# Given Two numbers. Multiply them and find the `Super Digit`

# `Super Digit is the digit formed by finding sum of digits of that number until it becomes single digit.`

# ```
# Input:
# 148 3

# Output: 3
# ```

a,b = list(map(int, input().split()))
n = a * b
print(9 if n % 9 == 0 else n % 9)

# Time Complexity - O(1)
# Space Complexity - O(1)
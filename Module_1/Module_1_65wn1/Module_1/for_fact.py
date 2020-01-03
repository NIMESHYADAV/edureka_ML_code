# Method 1: using for loop
val = int(input("enter the value:"))
out = 1
for elem in range(1, val+1):
    out *= elem

print(out)
# factorial: fact(5) 5*4*3*2*1

# Method 2: using recursion
"""
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
"""

print()
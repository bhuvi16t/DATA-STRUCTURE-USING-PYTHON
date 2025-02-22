#Recursion in DSA (Data Structures and Algorithms)
# What is Recursion?
# Recursion is a technique where a function calls itself to solve a problem. It is used when a problem can be broken down into smaller subproblems of the same type.

# Key Components of Recursion
# Base Case: The condition that stops the recursion and prevents infinite calls.
# Recursive Case: The part where the function calls itself with a smaller problem.


# for Example 
def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)

result = fact(5)
print(result)
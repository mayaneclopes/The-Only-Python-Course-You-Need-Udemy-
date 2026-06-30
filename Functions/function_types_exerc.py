# Function Types
# You're building a Function Behavior Analyzer to showcase different types of Python functions in action. Implement the following:
# Pure Function
# Write a function pure_add(a, b) that takes two integers and returns their sum.
# It should not rely on or modify any external state.
# Impure Function
# Define a global variable counter.
# Implement impure_increment() that increases the counter and returns its value.
# Recursive Function
# Implement factorial_recursive(n) that returns the factorial of a given number using recursion.
# Handle base case correctly (e.g., factorial_recursive(0) = 1).
# Lambda Function with map()
# Write a function square_list(nums) that uses a lambda inside map() to return a new list with the squares of the numbers in the input list.

def pure_add(a, b):
    return a + b 
    
counter = 0

def impure_increment():
    global counter
    counter += 1
    return counter

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    print(factorial_recursive(0))

def square_list(nums): return list(map(lambda x: x ** 2, nums))

nums = [1, 2, 3]

print(square_list(nums))
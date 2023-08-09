

"""
Closures:
- Occur when a nested function references variables from its containing (enclosing) function's scope,
  even after the outer function has finished executing.
  This allows you to create functions that "remember" their context.
- Often used in decorators and when we want to encapsulate behavior.
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure)
result = closure(5)  # Remembers x from the outer function
print(result)

"""
Decorators: 
- Functions that modify the behavior of other functions. 
  They provide a clean and efficient way to add functionality to existing functions without modifying their code. 
- Common use cases include logging, authentication, and memoization.
"""
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, world!")

say_hello()

"""
Decorators with Arguments: 
- Advanced decorators can take arguments, allowing us to create more flexible and customizable decorators. 
- This involves creating a series of nested functions to handle the various levels of parameter passing.
"""
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))

"""

Generator Functions: Generator functions use the yield keyword to produce a series of values on-the-fly, one at a time, instead of generating a complete list or sequence in memory. This is especially useful for dealing with large datasets or infinite sequences.

Decorators with Arguments: Advanced decorators can take arguments, allowing you to create more flexible and customizable decorators. This involves creating a series of nested functions to handle the various levels of parameter passing.

Function Factories: Function factories are functions that create and return other functions. They're particularly useful when you need to generate similar functions with slight variations.

Partial Functions: Partial functions are created by fixing a certain number of arguments of a function and generating a new function with fewer parameters. This is useful when you have a function with many arguments, and you want to create simpler versions with some parameters pre-set.

Currying: Currying is a technique where a function that takes multiple arguments is transformed into a sequence of functions that each take a single argument. This can be used for functional composition and creating specialized functions.

Lambda Functions and Sorting: Lambda functions can be used as key functions in sorting to customize the sorting order based on specific criteria.

Function Annotations: Python supports adding metadata annotations to function parameters and return values. These annotations can be used to provide type hints or additional information about the function's purpose.

First-Class Functions and Higher-Order Functions: Understanding the concept of first-class functions (functions treated as objects) and higher-order functions (functions that take other functions as arguments or return them as results).

Recursion: Recursion is the process of a function calling itself. It can be a powerful technique for solving problems that can be broken down into smaller instances of the same problem.

Anonymous Functions and Map-Reduce-Filter: Lambda functions are often used in combination with map, reduce, and filter functions for concise and functional-style data processing.
"""

# Decorators with Arguments:
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# Partial Functions:
import functools

def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(square(5))  # Output: 25
print(cube(3))    # Output: 27


# Generator Functions:
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))


# Lambda Functions and Sorting:
data = [("apple", 3), ("banana", 1), ("cherry", 2)]
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data)  # Output: [('banana', 1), ('cherry', 2), ('apple', 3)]

# Function Annotations:
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

# # Python Generator

# def generator_func():
#     yield 1
#     yield 2
#     yield 3
# gen = generator_func()
# # print(next(gen))
# # print(next(gen))
# for i in gen:
#     print(i)

# # Memory Usage : List vs generator
# import sys
# list_nums = [i for i in range(1000000)]
# print(f"Size = {sys.getsizeof(list_nums)} bytes")

# gen_nums = [i for i in range(1000000)]
# print(f"Size = {sys.getsizeof(gen_nums)} bytes")

# # Python Decorator
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function {func.__name__} with {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print("function Called")
#         return result
#     return wrapper

# @log
# def add(num1, num2):
#     print(num1 + num2)

# @log
# def say_hello():
#     print("Hello World!")

# add(1,2)
# say_hello()

# import time
# print()


#Exception Handling

# def log(func):
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             print(f"An error occurred in {func.__name__}: {e}")
#     return wrapper

# @log
# def add(num1, num2):
#     # print(num1 + num2)
#     print(num1 / num2)

# @log
# def say_hello():
#     print("Hello World!")

# # add(1, 2)
# add(1, 0)
# say_hello()


# # Recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))


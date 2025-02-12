#function

def add():
    num1 = 10
    num2 = 20
    print(num1 + num2)
add()
add()


def add(num1, num2):
    #print(num1 + num2)
    return num1 + num2
a = add(1, 2)
b = add(12, 15)
print(a)
print(b)


def calculate(num1, num2):
    sum = num1 + num2
    sub = num1 - num2
    prod = num1 * num2
    return sum , sub , prod
a, b, c = calculate(20, 10)
print(a)
print(b)
print(c)


#lambda function

add = lambda a,b: a + b
print(add(1,2))


# to print multiplication table from 2 to 5

def multiplication_tables(start, end):
    for num in range(start, end + 1):  
        print(f"\nMultiplication Table of {num}")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")

multiplication_tables(2, 5)

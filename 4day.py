#for loop

for i in range(10):
    print(i)

for i in range(1, 10):
      print(i, end=" ")
      #print(i, end="\n")
#     #print(i)

for i in range(1, 10,2):
    print(i)

for i in range(10):
     print("python")


#factorial

num = int(input("Enter a number: "))
fact = 5
for i in range(1, num+1):
    fact = fact * i
print(fact)


#while loop
num = int(input("Enter number: "))
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1
print(fact)


#Break
for i in range(10):
    if i == 3:
        break
    print(i)

for i in range(10):
    print(i)
    if i == 3:
        break
    

#Continue
for i in range(10):
    if i == 3:
        continue
    print(i)
    #print(i, end= " ")

for i in range(10):
    if i == 3:
        #print(i)
        print(i, end= " ")


#pass
for i in range(5):
    pass
    print(i)


#practice question: 

#1.  sum of first n numbers

def sum_of_n_numbers(n):
    return n * (n + 1) // 2
n = 10
print("The sum of the first", n, "numbers is:", sum_of_n_numbers(n))


#2.  prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True

print(is_prime(11))  
print(is_prime(15))  


#3.  palindrome number
def check_palindrome(num):
    rev_num = 0
    original_num = num
    while num > 0:
        rem = num % 10
        num = num // 10
        rev_num = rev_num * 10 + rem
    if rev_num == original_num:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome(121)
check_palindrome(123)


# #4.  1 to 100 even numbers
for number in range(1, 101):
    if number % 2 == 0:
         print(number)
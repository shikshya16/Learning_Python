#to take input from user

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(num1)
print(num2)
print(num1 + num2)


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)


#Conditional Statements(if..elif..else)

age = 11
if age >= 18: 
    print("He/She can vote")
else:
    print("He/She cannot vote")


age = -1
if age >= 18: 
    print("He/She can vote")
elif age <= 0:
    print("Invalid age")
else:
    print("He/She cannot vote")


age = 22
if age >= 18 and age < 65:
    print("You can vote")
elif age <= 0:
    print("Invalid age")
else:
    print("You cannot vote")

#Practice Question:

#1.  odd or even

num = int(input("Enter number: "))
if num % 2 == 0:
    print("It is even number")
else:
    print("It is odd number")


#2.  profit loss

SP = float(input("Enter SP: "))
CP = float(input("Enter CP: "))
if SP > CP:
    print("Profit: ")
    print(SP - CP)
else: 
    print("loss: ")
    print(CP - SP)


#3.  to find largest number among three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Number 1 is greater")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is greater")
else:
    print("Number 3 is greater")



#4.  to assign the grade based on the marks

marks = float(input("Enter the marks: "))
if marks >= 90:
    print ("A+")
elif marks >= 80:
    print ("A")
elif marks >= 70:
    print ("B+")
elif marks >= 60:
    print ("B")
elif marks >= 50:
    print ("C+")
elif marks >= 40:
    print ("C")
elif marks >= 30:
    print ("D")
elif marks >= 20:
    print ("E")
else:
    print ("F")


#5.  to print fizz if a number is divisible by 3, Buzz if a number is divisible by 5
#fizzbuzz if number is divisible by both 5 and 3 else print the number as it is

num = int(input("Enter a number: "))

if num % 3 == 0 and num% 5 == 0:
    print("Fizz Buzz")

elif num % 5 ==0:
    print("Buzz")

elif num % 3 == 0:
    print("Fizz")

else:
    print(num)




#Tuples

numbers = (1,2,3,4)
print(numbers)
print(numbers[0])
print(numbers[-1])

numbers = (1,1,2,3,1,4)
print(numbers.count(1))
print(numbers.index(3))

numbers = (1,2,3,4)
for num in numbers:
    print(num)

#TypeCasting

#converting tuple to list

numbers = (1,2,3,4)
print(type(numbers))
numbers = list(numbers)
print(type(numbers))
print(numbers)

#converting list to tuples
numbers = [1,2,3,4]
print(type(numbers))
numbers = tuple(numbers)
print(type(numbers))
print(numbers)


numbers = (1,2,3,4)
a,b,c,d,e = numbers
print(a)
print(c)
print(e)


#Dictionary

user = {
    'username' : 'poudelshikshya' ,
    'age' : '24' ,
    'password' : '12345' ,
    'is_verified' : True
}

for i in user:
    print(i)

for i in user.values():
    print(i)

for key, value in user.items():
    print(f"{key} -> {value}")

print(user)
print(user['username'])
print(user['password'])
print(user.get('age'))
print(user['address'])
print(user.get('address'))  #print(user.get('address', 'not found'))
print(user.get('age', 'not found'))

user['username'] = 'shikshya.poudel'
print(user['username'])

del user['is_verified']
print(user)

a= user.pop('is_verified')
print(a)
print(user)

print(user.keys())
print(user.values())


# Dictionary Comprehension

words = ['apple', 'banana', 'cherry', 'doll']
a = {key : len(key) for key in words}
print(a)

#Nested
user = {
    'username' : 'shikshya16',
    'age' : 24,
    'password' : '12345',
    'is_verified' : True,
    'address' : {
        'province' : 'Bagmati',
        'District' : 'Kathmandu'
    }
}

print(user['address']['province'])
print(user['address']['District'])
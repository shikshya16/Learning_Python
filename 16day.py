import json
user = {
    "username" : "Shikshya",
    "password" : "password"
}
print(type(user))


import json
user = {
    "username" : "Shikshya",
    "password" : "password"
}
json_user = json.dumps(user, indent=4)
print(type(json_user))
print(json_user)


import json
user = {
    "username" : "Shikshya",
    "password" : "password"
}
with open('user.json', 'w')as file:
    json.dump(user, file, indent=4)


import json
with open('user.json') as file:
    chunk = ''
    for line in file:
        chunk = chunk + line
    print(chunk)
    print(type(chunk))


import json
with open('user.json') as file:
    chunk = ''
    for line in file:
        chunk = chunk + line
    user = json.loads(chunk)
    print(type(user))


import json
with open('user.json') as file:
    user = json.load(file)
    print(type(user))
    print(user)


#Map Function

numbers = [1,2,3,4,5,6]
cubed = list(map(lambda num: num ** 3, numbers))
print(cubed)
# for n in cubed:
#     print(n)


#filter function

numbers = [1,2,3,4,5,6]
even = list(filter(lambda num: num % 2 == 0, numbers))
print(even)


#Reduce Function

from functools import reduce
numbers = [1,2,3,4,5,6]
sum = reduce(lambda x,y: x+y, numbers)
print(sum)


#OS Library

import os
pwd = os.getcwd()
# print(pwd)
dirs = os.listdir(pwd)
os.remove('new.csv')
print(dirs)

#Random Library

import random
#print(random.randint(1000,9999))
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)


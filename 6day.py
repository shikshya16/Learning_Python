a = "Hello World!"
print(a[6])
print(a[-12])
print(a[0:5])
print(a[0:5:2])
print(a[:5])
print(a[5:])
print(len(a))


a = "Hello World!"
for i in range(len(a)):
    print(a[i])

for char in a:  #here, in is called membership operator 
    print(char)

#String Method 

a = "Hello World!"
print(a.replace("World", "python"))
print(a)
print(a.upper())
print(a.lower())
print(a.title())

a = "Hello World!"
a = "          Hello python!"
print(a.lstrip())
print(a.lstrip('H'))
print(a.rstrip())
print(a.strip())

data = 'a,b,c,d'
print(data.split(','))


fname = 'Shikshya'
lname = 'Poudel'
age = 23

print("My name is " + fname +" " + lname+ ".")
print(f"My name is {fname} {lname}. My age is {age}")  #fstring
print("My name is {} {}".format(fname, lname))




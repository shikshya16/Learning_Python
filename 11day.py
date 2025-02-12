#Set

a = {1,2,3,4,5}
b = {3,4,5,6,7,8,9,0}
a.add(7)
a.remove(4)
a.remove(14)
a.discard(5)
a.discard(15)
print(a)
print(a | b) #union
print(a & b) #intersection
print(a - b) #difference
print(a ^ b) #symmetric difference (A-B)U(B-A)

a = {}
b = []
c = ()
d = set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# remove duplicate numbers

a = [1,2,3,1,2,1]
#print(set(a))
print(list(set(a)))

def sum(num1, num2=0):
    print(num1 + num2)
#sum(1)
sum(1, 6)

def sum(*args):
    #print(args)
    result = 0
    for i in args:
        result = result + i
    print(result)
sum(1,2,3)
sum(1)

def sum(*args, **kwargs):
    print(args)
    print(kwargs)

sum(1,2,3,4,5,6,7, num1=1, num2=3, name="shikshya")


def a(num1, num2):
    pass
a(num2=1, num1=2)
#list

numbers = [1,2,3,4,5,6,7,8,9,0]
print(numbers)
print(numbers[5])
print(len(numbers))
print(numbers[1:5:2])
print(numbers[::-1])
print(numbers[::-2])
for num in numbers:
    print(num)


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#print(matrix[0][-1])

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()


numbers = [1,2,3,4,5,6,7]
numbers2 = [8,9,0]
numbers.append(10)
numbers.append(1)
numbers.pop()
numbers.pop(1)
numbers.insert(2, 0)
numbers.remove(3)
numbers.extend(numbers2)
print(numbers)
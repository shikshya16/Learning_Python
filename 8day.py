# #to find square number

# sq = []
# for i in range(1, 11):
#     sq.append(i ** 2)
# print(sq)

# #list Comprehension

# sq = [i ** 2 for i in range(1, 11)]
# print(sq)


# #to print square number of even number only

# sq = [i ** 2 for i in range(1, 11) if i ** 2 % 2 == 0]
# print(sq)


# [None, 2,  None, 4, None, 6, None, 8]
# for i in range(1, 9):
#     if i % 2 == 1:
#         print("None")
#     else:
#         print(i)


# [None, 4,  None, 16, None, 36, None, 64]
# for i in range(1, 9):
#     if i % 2 == 1:
#         print("None")
#     else:
#         print(i ** 2)

# [None, 2,  None, 4, None, 6, None, 8]
# a = [i if i%2 == 0 else None for i in range(1,9)]
# print(a)

# #Practice Question

# #1.  min and max number
# a = [11, 202, 345, 46, 76, 88]
# print("The minimum number is" , min(a))
# print("The maximum number is", max(a))

# a = [11, 202, 345, 46, 76, 88]
# min = a[0]
# max = a[0]
# for num in a:
#     if num > max:
#         max = num
#     if num < min:
#         min = num
# print(f"Min = {min} and Max = {max}")


# #2.  remove duplicate content

# dup_numbers = [1,2,3,4,5,6,3,2,5,7,8,9]
# numbers = []
# for num in dup_numbers:
#     if num not in numbers:
#         numbers.append(num)
# print(numbers)

# #3.  union, intersection
# a = [1,2,3,4]
# b = [3,4,5,6]
# new_set = a + b
# union = []
# intersection = []
# for num in new_set:
#     if num not in union:
#         union.append(num)
#     else:
#         intersection.append(num)
# print("The union is " , union)
# print("The intersection is " ,intersection)


# [1,2,3,4,5], target_sum = 5
# num = [1, 2, 3, 4, 5]
# target_sum = 5

# pairs = []
# for i in range(len(num)):
#     for j in range(i + 1, len(num)):  
#         if num[i] + num[j] == target_sum:
#             pairs.append((num[i], num[j]))

# print("Pairs that sum to", target_sum, ":", pairs)

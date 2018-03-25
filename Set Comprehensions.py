nums = [1, 1, 2, 2, 7, 3, 4, 5, 6, 3, 7, 8, 7, 9, 10, 9]

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

my_set = {n for n in nums}
print(my_set)
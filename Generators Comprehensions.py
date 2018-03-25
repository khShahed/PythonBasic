
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# I want to yield n*n for each n in nums

# def gen_func(numbers):
#     for n in numbers:
#         yield n*n
#
# my_gen = gen_func(nums)
#
# for i in my_gen:
#     print(i)


my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
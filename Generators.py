
# def square_numbers(nums):
#     results = []
#     for i in nums:
#         results.append(i*i)
#     return results
#
# my_nums = square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(my_nums)

# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)
#
# my_nums = square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
# # my_nums = [x*x for x in [1, 2, 3, 4]] # List
# my_nums = (x*x for x in [1, 2, 3, 4]) # Generator
# print(my_nums)
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums))
# # print(next(my_nums)) # error
#
# for num in my_nums:
#     print(num)

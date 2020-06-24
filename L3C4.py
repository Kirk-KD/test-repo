# # Homework
# # 1)
# my_dict = {"a":1, "b":2, "c":3}
# try:
#     my_dict["d"]
# except KeyError:
#     pass

# # 2)
# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[6]
# except IndexError:
#     pass

# try:
#     f = open("f.txt")
#     var = badvar
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("finally")

# x = 10
# y = "hi"
# z = "Hello"
# print(y)
# breakpoint()
# print(z)

# for i in range(10):
#     print(f"i = {i}")
#     if i == 5:
#         breakpoint()

# def debug(a, b):
#     import pdb; pdb.set_trace()
#     result = a / b
#     return result
# print(debug(3, 0))

# def square(n):
#     """
#     Returns the square of n.
#     """
#     return n ** 2
# print(square.__doc__)

# numerator = 10
# denominator = 3
# assert denominator != 0
# result = numerator


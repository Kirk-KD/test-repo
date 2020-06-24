# a = int(input("a: "))
# b = int(input("b: "))

# try:
#     res = a / b
#     print(f"res: {res}")
# except:
#     print("handled")

# import sys
# try:
#     num = int ( input('Enter the numerator ') )
#     den = int ( input('Enter the denominator ') )
#     try:
#         result = num/den
#         print('Result =',result)
#     except:
#         print('Divide by Zero Error')
# except:
#     print('Invalid Input')

# print('End of program')

# try:
#     print("Marks: ")
#     marks = int(input())

#     if marks < 0 or marks > 100:
#         raise ValueError
# except ValueError:
#     print("out of range")

# try:
#     a = int(input("num1: "))
#     b = int(input("num2: "))

#     res = a / b
#     print(f"res: {res}")
# except (ValueError, TypeError):
#     print("invalid input err")
a = "opt \"hi\""
for i in range(len(a)):
    print(a[i-1])
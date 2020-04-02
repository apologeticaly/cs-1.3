import sys

number = '2'
def binary(number):
   """Function to print binary number
   for the input decimal using recursion"""
   x = int(number)
   if x > 1:
       binary(x // 2)
   return x % 2


if __name__ == "__main__":
    print(binary(number))       
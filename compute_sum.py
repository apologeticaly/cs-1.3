# Write a function called compute_sum() that takes in a single integer
# argument n and returns the sum of the positive integers from 1 to n.
# For example compute_sum(4) would return 10, or 1+2+3+4. You need to
# use a loop to complete this function. Upload your .py file when you are done.

num = 500

def compute_sum(num):
    fib = 0
    operand = num

    while operand > 0:
        fib = fib + operand
        operand = operand - 1

    if operand == 0:
        return fib

print(compute_sum(num))

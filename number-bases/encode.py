number = 100
def b(number):
    if number > 1: 
        b(number // 2) 
    return number % 2

print(b(number))


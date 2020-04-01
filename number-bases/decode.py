def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # ...

    list_digits = list(digits)
    if base == 2:
        value = 0
        for i in range(len(list_digits)):
            list_digit = list_digits.pop()
            if list_digit == '1':
                value = value + pow(2, i)
        return(value) 

    # # TODO: Decode digits from hexadecimal (base 16)
    # # ...
    
    if base == 16:
        value = 0
        for i in range(len(list_digits)):
            list_digit = list_digits.pop()
            
            if list_digit == "A":
                value = value + pow(16, i) * 10

            if list_digit == "B":
                value = value + pow(16, i) * 11

            if list_digit == "C":
                value = value + pow(16, i) * 12

            if list_digit == "D":
                value = value + pow(16, i) * 13

            if list_digit == "E":
                value = value + pow(16, i) * 14

            if list_digit == "F":
                value = value + pow(16, i) * 15

            else:
                value = value + pow(16, i) * int(list_digit)

        return(value) 
    
    else:
        value = 0
        for i in range(len(list_digits)):
            list_digit = list_digits.pop()
            
            value = value + pow(base, i) * int(list_digit)
                
        return(value) 
        


    # # TODO: Decode digits from any base (2 up to 36)
    # # ...

    # else:
    #     return int(digits, base)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    digits = args[0]
    base = int(args[1])
    # Convert given digits between bases
    result = decode(digits, base)
    print('{} in base {} is {} in base {}'.format(digits, base, result, 10))

if __name__ == '__main__':
    main()
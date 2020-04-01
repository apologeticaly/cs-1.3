import sys

def dec_to_hex(n):
    x = (n % 16)

    numbers = "0123456789ABCDEF"

    remainder = n // 16

    if remainder == 0:
        return numbers[x]

    return dec_to_hex(remainder) + numbers[x]


if __name__ == "__main__":
    n = int(sys.argv[1])
    print (dec_to_hex(n))         
def stack(nums=123456789):
    input = list(str(nums))
    output = []

    for i in range(len(input)):
        output.append(input.pop())

    print("".join(output))

stack()
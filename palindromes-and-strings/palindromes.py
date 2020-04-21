#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_letters is string.ascii_lowercase + string.ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    index_x = 0
    index_y = (len(text) - 1)

    while index_x <= index_y:
        while text[index_x] not in string.ascii_letters:
            index_x += 1

        while text[index_y] not in string.ascii_letters:
            index_y -= 1

        if text[index_x].lower() != text[index_y].lower():
            return False

        index_x += 1
        index_y -= 1

    return True
        
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if left == None and right == None:
        left = 0
        right = (len(text) - 1)

    if left <= right:
        if text[left] not in string.ascii_letters:
            left += 1
            return is_palindrome_recursive(text, left, right)

        if text[right] not in string.ascii_letters:
            right -= 1
            return is_palindrome_recursive(text, left, right)
        
        if text[left].lower() != text[right].lower():
            return False
        
        left += 1
        right -= 1
        return is_palindrome_recursive(text, left, right)

    return True
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
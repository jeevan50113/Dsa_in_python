def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))   # Output: True
print(is_palindrome("hello"))   # Output: False

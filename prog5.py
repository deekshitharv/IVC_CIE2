def is_palindrome_string(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(is_palindrome_string("PalindromeOrNotPalindrome"));   
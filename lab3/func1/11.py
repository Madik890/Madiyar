def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Ignore spaces and case
    return s == s[::-1]
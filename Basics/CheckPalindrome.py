def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")

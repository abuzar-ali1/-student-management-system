import re

def is_palindrome(text):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to check: ")
    if is_palindrome(user_input):
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")
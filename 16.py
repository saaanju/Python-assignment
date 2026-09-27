def check_palindrome(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    if text == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

text = input("Enter a string: ")
check_palindrome(text)
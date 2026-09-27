def count_case(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0

    for ch in text:
        if ch.isupper():
            uppercase = uppercase + 1
        elif ch.islower():
            lowercase = lowercase + 1
        elif ch.isdigit():
            digits = digits + 1
        elif ch == " ":
            spaces = spaces + 1

    print("Uppercase :", uppercase)
    print("Lowercase :", lowercase)
    print("Digits :", digits)
    print("Spaces :", spaces)

text = input("Enter text: ")
count_case(text)
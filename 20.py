def convert_uppercase(text):
    print("Using upper():", text.upper())

    result = ""

    for ch in text:
        if 'a' <= ch <= 'z':
            result = result + chr(ord(ch) - 32)
        else:
            result = result + ch

    print("Using loop:", result)

text = input("Enter a string: ")
convert_uppercase(text)
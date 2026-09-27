def reverse_string(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    print("Using loop:", reverse)
    print("Using slicing:", text[::-1])

text = input("Enter a string: ")
reverse_string(text)
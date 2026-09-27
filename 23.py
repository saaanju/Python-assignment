def last_character(text):
    print("Using indexing:", text[-1])

    last = ""

    for ch in text:
        last = ch

    print("Using loop:", last)

text = input("Enter a string: ")
last_character(text)
def display_position(text):
    for i in range(len(text)):
        print("Position", i, ":", text[i])

text = input("Enter a string: ")
display_position(text)
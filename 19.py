def remove_spaces(text):
    result = ""

    for ch in text:
        if ch != " ":
            result = result + ch

    return result

text = input("Enter a string: ")
print(remove_spaces(text))
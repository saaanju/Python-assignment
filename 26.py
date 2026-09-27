def remove_vowels(text):
    result = ""

    for ch in text:
        if ch.lower() not in "aeiou":
            result = result + ch

    return result

text = input("Enter a string: ")
print(remove_vowels(text))
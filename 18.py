def character_frequency(text, ch):
    count = 0

    for character in text:
        if character == ch:
            count = count + 1

    return count

text = input("Enter text: ")
ch = input("Enter character: ")

print("Frequency =", character_frequency(text, ch))
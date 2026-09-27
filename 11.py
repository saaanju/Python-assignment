def count_characters(text):
    count = 0

    for ch in text:
        count = count + 1

    return count

text = input("Enter a string: ")
print("Characters =", count_characters(text))
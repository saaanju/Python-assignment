def count_consonants(text):
    count = 0

    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou":
            count = count + 1

    return count

text = input("Enter a string: ")
print("Consonants =", count_consonants(text))
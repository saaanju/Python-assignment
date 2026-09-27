def find_longest_word(text):
    longest = ""
    current = ""

    for ch in text:
        if ch != " ":
            current = current + ch
        else:
            if len(current) > len(longest):
                longest = current
            current = ""

    if len(current) > len(longest):
        longest = current

    return longest

text = input("Enter a sentence: ")
print("Longest word =", find_longest_word(text))
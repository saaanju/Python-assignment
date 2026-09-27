def count_words(text):
    count = 0
    in_word = False

    for ch in text:
        if ch != " " and in_word == False:
            count = count + 1
            in_word = True
        elif ch == " ":
            in_word = False

    return count

text = input("Enter a sentence: ")
print("Words =", count_words(text))
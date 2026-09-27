def count_vowels(text):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for ch in text.lower():
        if ch == "a":
            a = a + 1
        elif ch == "e":
            e = e + 1
        elif ch == "i":
            i = i + 1
        elif ch == "o":
            o = o + 1
        elif ch == "u":
            u = u + 1

    print("a =", a)
    print("e =", e)
    print("i =", i)
    print("o =", o)
    print("u =", u)

text = input("Enter a string: ")
count_vowels(text)
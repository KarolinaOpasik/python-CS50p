def main():
    text = input("Input: ")
    output = shorten(text)
    print("Output:", output)


def shorten(word):
    shorten_word = ""
    vowels = "a", "e", "u", "i", "o"
    for c in word:
        if c not in vowels:
            shorten_word += c
    return shorten_word


main()

def main():
    text = input("Text: ")
    result = convert(text)
    print(result)


def convert(face):
    face = face.replace(":)", "🙂").replace(":(", "🙁")
    return face


main()

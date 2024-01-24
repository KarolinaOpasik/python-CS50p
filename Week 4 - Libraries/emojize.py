import emoji

emoji_name = input("Input: ")
output = emoji.emojize(emoji_name, language = "alias")

print("Output: ", output)

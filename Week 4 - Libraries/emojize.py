# https://cs50.harvard.edu/python/2022/psets/4/emojize/

import emoji

emoji_name = input("Input: ")
output = emoji.emojize(emoji_name, language = "alias")

print("Output: ", output)

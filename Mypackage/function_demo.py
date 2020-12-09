def emoji_converter(msg):
    words = msg.split()
    dict_mapping = {
        ":)": "😀",
        ":(": "😌"
        }
    output = ""
    for word in words:
        output += dict_mapping.get(word, word) + " "

    return output



message = input(">")
result = emoji_converter(message)
print(result)
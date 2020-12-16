phone = (input("enter phone number"))

dict_mapping = {
    "1": "one",
    "2":"Two",
    "3":"Three",
    "4":"four"
        }
output = " "
for ch in phone:
   output += dict_mapping.get(ch, "!") + " "


print(output)

message = input(">")
words = message.split(' ')
print(words)

emojis = {
    ":)": "😀",
    ":(":"😌"
}
output = " "
for word in words:
    output += emojis.get(word, word) + " "

print(output)
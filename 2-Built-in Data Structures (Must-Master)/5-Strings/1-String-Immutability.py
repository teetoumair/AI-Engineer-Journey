#1-String-Immutability.py

"""text = "hello" banao, text.upper(), text.capitalize(), text.replace("l", "x") teeno run karo aur results variable mein store karke print karo
Phir original text print karo — dekho kya woh change hua?
text[0] = "H" try karo — kya hoga?
text + " world" print karo — kya ye original ko change karega?"""

text = "hello"

upper = text.upper()
replacement = text.replace("l","x")

print(upper)
print(replacement)
print(text)


#Will give errors
#text[0] = "H"

new_string = text + " world"

print(new_string.capitalize())
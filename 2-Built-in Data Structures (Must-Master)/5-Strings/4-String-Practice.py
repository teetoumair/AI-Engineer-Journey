#4-String-Practice.py

text = "  welcome to THE ai Engineer Roadmap 2026  "

"""
Spaces trim karo (start/end)
Start se pehla word print karo ("welcome") — slicing se
Last word print karo ("2026")
Poore text ko title case mein print karo ("Welcome To The Ai Engineer Roadmap 2026")
Poore text ka reverse print karo
"""

stripped_text = text.strip()

print(stripped_text)
print(stripped_text[0:7])
print(stripped_text[-4:])
print(stripped_text.title())
print(stripped_text[::-1])
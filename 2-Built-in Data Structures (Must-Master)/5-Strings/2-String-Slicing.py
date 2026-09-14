#2-String-Slicing.py

"""
word[0:3], word[3:], word[-3:] print karo
Reverse print karo
word[0:5:2] — kya dega? (0 se 4 tak, har 2nd char)
"Py" aur "on" alag slices se le kar + se jodo aur print karo
"""

word = "Python"

print(word[0:3])
print(word[3:])
print(word[-3:])
print(word[::-1])
print(word[0:5:2])
py = str(word[0:2])
on = str(word[4:6])

print(py + " " + on)
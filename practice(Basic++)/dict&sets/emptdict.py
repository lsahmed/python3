# Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

dict = {}
name = input("Enter friend name: ")
lang = input("Enter language name: ")
dict.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
dict.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
dict.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
dict.update({name: lang})

print(dict)
# Create an empty dictionary.Allow 4 friends to enter their favourite language as value and use key as their name.Assume that names are unique

d={}
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})

print(d.items())

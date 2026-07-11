# If the names of 2 friends are same, what will happen to the program in problem 6

d={}
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")       # old value will get updated and replaced by new value
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})

print(d.items())

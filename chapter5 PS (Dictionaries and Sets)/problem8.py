# if the languages of 2 friends are same,what will happen to the program in problem 6

d={}
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")          #values can be same, all elements will be printed
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})
name=input("Enter your name:")
lang=input("Enter your favourite language:")
d.update({name:lang})

print(d.items())

# WAP to create a dictionary of Hindi words with values as their english translation.Provide user with an option to look it up!

dict={
    "aam":"mango",
    "kela":"banana",
    "madad":"help",
    "kursi":"chair"
}
print(dict.keys())
word= input("You can search any word from this list:")


print(f"English transaltion of {word} is {dict.get(word)}. ")


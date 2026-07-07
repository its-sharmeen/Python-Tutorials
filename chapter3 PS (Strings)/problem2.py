# WAP to fill a letter template given below with name and date
letter ='''
      Dear <|Name|>,
     You are selected!
       <|Date|>
       '''

name=input("Write your name:")
date=input("Write date:")
print(f""" Dear {name},
      You are selected ! 
      {date}
""")

# OR

print((letter.replace("<|Name|>",name)).replace(" <|Date|>",date))  #chaining of string function

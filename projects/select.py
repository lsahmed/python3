dicti = {"Ilsa": 1100, 
        "Rohan":1122,
        "Ahmed":1133}
name = input("Enter your name: ")
roll = int(input("Enter your roll no. : "))

#Block of code which gives the key from value
key_list = list(dicti.keys())
val_list = list(dicti.values())
posit = val_list.index(roll)
keyos = key_list[posit]

if(name in dicti) and (keyos in dicti):
  print("You are selected")
else:
  print("Better luck next time")

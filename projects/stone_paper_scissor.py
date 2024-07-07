import random
comp = random.randint(0,2)
youstr = input("Enter the what you choose stone or paper or scissor: "  )
dict = {"stone": 0, "paper": 1, "scissor": 2}
you = dict.get(youstr)

if(comp==0 and you==1):
  print("You wins")
elif(comp==0 and you==2):
  print("You loose")
  
elif(comp==1 and you==0):
  print("You loose")
elif(comp==1 and you==2):
  print("You win!")

elif(comp==2 and you==0):
  print("You win")
elif(comp==2 and you==1):
  print("you loose! ")

else:
  print("Match tie")

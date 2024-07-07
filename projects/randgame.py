import random;

num = random.randint(1,5)
inp = int(input("Guess the number between 1 and 5: "))
if(inp==num):
  print("you guess correctly")
else:
  print("better luck next time")
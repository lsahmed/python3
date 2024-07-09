# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random

def game(score):
    print(f"Your score is {score}")
    with open("scores.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    if(score>int(hiscore) or hiscore==""):
        with open("scores.txt","w") as f:
            f.write(str(score))

score = random.randint(1,100)
game(score)
    

import random

def game():

    print("You Are Playing A Game !")

    score = random.randint(1, 62)

    with open("hiscore.txt") as f:
        
        hiscore = f.read()

        if(hiscore !=""):
           
           hiscore = int(hiscore)
        else:
           
           hiscore = 0

    if(score>hiscore):
      
      print(f"Your Score Is : {score}")

    with open("hiscore.txt", "w") as f:
        
       f.write(str(score))
    
    return score

game()
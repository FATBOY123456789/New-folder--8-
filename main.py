import random
class Fruitquiz:
    def __init__(self):
        self.fruits={'Apple':'red','Banana':'yellow','Watermelon':'green','Orange':'orange'}
    def quiz(self):
        while True:
            fruit,colour=random.choice(list(self.fruits.items()))
            print('What is the colour of',format(fruit))
            user_answer=input()
            if (user_answer.lower()==colour):
                print('Correct!')
            else:
                print('Wrong.')
            option=int(input('Do you wish to play again? 1 for YES, 0 for NO.'))
            
            if option==0:
                break
print('Welcome to the fruit quiz!')
fq=Fruitquiz()
fq.quiz()
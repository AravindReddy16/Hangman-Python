import random

class Hangman:
    def __init__(self):
        self.pic=[
            ' ________',
            '|        |',
            '|        O',
            '|        |',
            '|       /|\\',
            '|        |',
            '|       /|\\',
            '|',
        ]
        self.words=['python','django','cloths','planes','charges','phones']
        self.inc=0
        self.w=list(random.choice(self.words))
        self.r=random.choice(self.w)
        self.ls=list()
        for i in self.w:
            if i==self.r:
                self.ls.append(i)
            else:
                self.ls.append('_')
    def picls(self):
        for i in range(self.inc):
            print(self.pic[i])
        print()
    def word(self):
        j=' '.join(self.ls)
        print(j)
        print()
    def play(self):
        self.word()
        while True:
            e=input('Enter Word: ')
            if self.inc!=7:
                if e in self.w:
                    self.picls()
                    if e not in self.ls:
                        s=self.w.index(e)
                        self.ls[s]=e
                        self.word()
                        if self.ls==self.w:
                            print('You Won Game !...')
                            print()
                            break
                    else:
                        print('Already given the Letter....')
                        print()
                else:
                    self.inc+=1
                    self.picls()
                    self.word()
            else:
                print()
                print('You Lose Game !...')
                print()
                break
oGame=Hangman()
oGame.play()
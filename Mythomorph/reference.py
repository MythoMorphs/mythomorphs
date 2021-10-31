"""Georgia Institute of Technology - CS1301
Homework 10 - Object Oriented Programming"""

class Mario:
    def __init__(self, name, lives=3, coins=0, isAlive = True):
        self.name = name
        self.lives = lives
        self.coins = coins
        self.isAlive = isAlive
    # the following method is provided to you

    def gainCoins(self,ncoin=5):
        self.coins=self.coins+ncoin

    def loseLife(self):
        if self.lives>0:
            self.lives -= 1
        if self.lives == 0:
            self.isAlive = False

    def gainLife(self):
        if self.lives > 0 and self.lives < 3:
            self.lives += 1
        elif self.lives >= 3:
            self.coins += 10

    def __str__(self):
        return "Hi! I am {self.name}. I have {self.lives} lives left and {self.coins} coins.".format(self=self)

    def __eq__(self, other):
        return self.name == other.name and self.lives == other.lives and self.coins == other.coins and self.isAlive == other.isAlive
    # the following method is provided to you
    def __repr__(self):
        return f"Mario({self.name})"
###########################################################

class Bowser:
    def __init__(self, name, lives=5, isAlive=True):
        self.name=name
        self.lives=lives
        self.isAlive=isAlive
    # the following method is provided to you

    def loseLife(self):
        if self.lives>0:
            self.lives -= 1
        if self.lives == 0:
            self.isAlive = False

    def __str__(self):
        return "Hi! I am {self.name} and I have {self.lives} lives left.".format(self=self)

    def __eq__(self, other):
        return (self.name == other.name and
        self.lives == other.lives and
        self.isAlive == other.isAlive)
    # the following method is provided to you
    def __repr__(self):
        return f"Bowser({self.name})"
###########################################################

class World:
    def __init__(self, name, bowser, characters=(), isWon= False ):
        self.name = name
        self.characters = characters
        self.bowser = bowser
        self.isWon = isWon

    def __str__(self):
        if self.isWon == False:
            return "{self.name} has not been won yet.".format(self=self)
        else:
            return "{self.name} has been won!".format(self=self)

    def addChar(self,mchar):
        self.characters=list(self.characters)
        a=True
        for entry in self.characters:
            if entry.name == mchar.name:
                a=False
                self.characters = tuple(self.characters)
                return mchar.name + " already exists in {self.name}.".format(self=self)
        if a==True:
            self.characters.append(mchar)
        self.characters=tuple(self.characters)

    def removeChar(self,mchar):
        self.characters=list(self.characters)
        if mchar in self.characters:
            self.characters.remove(mchar)
        self.characters=tuple(self.characters)
        if self.characters == ():
            self.gameOver()

    def runInto(self, pu, mchar):
        if pu == "mushroom":
            mchar.gainLife()
        elif pu == "goomba":
            mchar.loseLife()
            if mchar.lives == 0:
                self.removeChar(mchar)
        elif pu == "coin":
            mchar.gainCoins(5)

    def fight(self,mchar,bowser,win):
        if win == True:
            mchar.gainCoins(20)
            bowser.loseLife()
            if bowser.isAlive == False:
                self.gameOver()
        if win == False:
            mchar.loseLife()
            if mchar.isAlive == False:
                self.removeChar(mchar)

    def gameOver(self):

        if self.characters == () and self.bowser.isAlive:
            print("Mario Team loses.")
        if self.bowser.isAlive == False:
            print("Mario Team wins!")

    # the following method is provided to you
    def __repr__(self):
        return f"World({self.name}, {self.bowser})"



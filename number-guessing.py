#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import seed
from random import randint

class Player:
    "This is the player class representing the player"
    _name = ""
    _points = 0
    
    def __init__(self, name = ""):
        self._name = name
    
    def tellName(self):
        if self._name == "":
            print("Sadly I don't have a name yet. :(")
        else:
            print("My name is {0}.".format(self._name))
    
    def setName(self, name):
        self._name = name

class Game:
    "This is the actual game"
    _player = None
    _npc = None
    _maxNumberOfGuesses = 0
    _currentNumberOfGuesses = 0
    _rounds = 0
    _minNumber = 0
    _maxNumber = 0
    
    def __init__(self, player, npc, maxNumberOfGuesses, minNumber, maxNumber):
        self._player = player
        self._npc = npc
        self._maxNumberOfGuesses = maxNumberOfGuesses
        self._minNumber = minNumber
        self._maxNumber = maxNumber
    
    def launch(self):
        print("Hello my dear. Ready to play a litte game? I am bored.")
        if self.getStartGameInput():
            self.startNewGame()
            
    def getStartGameInput(self):
        answer = input("Answer with 'y'es or 'n'o: ")
        if answer == "y":
            print("Perfect! We will have so much fun.")
            return True
        elif answer == "n":
            print("This makes me sad. Please go away.")
            return False
        elif answer == "":
            print("I didn't hear you. Speak up please.")
            return self.getStartGameInput()
        else:
            print("What did you say? This makes no sense")
            return self.getStartGameInput()
            
    def startNewGame(self):
        self.askForName()
        print("So this is your name? I like it!")
        print("Let's get started.")
        self.explainRules()
        self.startNewRound()
    
    def askForName(self):
        print("But first of all: Please tell my your name?")
        self._player.setName(self.getNameInput())
        self._player.tellName()
        
    
    def getNameInput(self):
        result = input()
        if result == "":
            print("I didn't hear you. Speak up please.")
            return self.getNameInput()
        return result
    
    def explainRules(self):
        print("I select a number between {0} and {1}.".format(self._minNumber, self._maxNumber))
        print("You will guess this number!")
        print("If you have guessed the correct number, you win this round")
        print("If you guessed wrong {0} times I win.".format(self._maxNumberOfGuesses))
        print("But don't worry. I will give you a hint if you guess wrong")
    
    def startNewRound(self):
        self._rounds = self._rounds + 1
        Round(self).start()
        self.tellScore()
        self.askForAnotherRound()
        
    def tellScore(self):
        print("Player {0} has {1} points. Player {2} has {3} points.".format(
            self._player._name, self._player._points, self._npc._name, self._npc._points))
        
    def askForAnotherRound(self):
        print("Do you like to play another round?")
        if self.getAnotherRoundInput():
            self.startNewRound()
        
    def getAnotherRoundInput(self):
        answer = input("Answer with 'y'es or 'n'o. ")
        if answer == "y":
            print("Perfect! Let's continue.")
            return True
        elif answer == "n":
            print("OK. This was fun. Let's play again some time. Bye!")
            return False
        elif answer == "":
            print("I didn't hear you. Speak up please.")
            return self.getStartGameInput()
        else:
            print("What did you say? This makes no sense")
            return self.getStartGameInput()
        
class Round:
    "This class represents one round of the Game. A match my consist of multiple rounds"
    _currentNumberOfGuesses = 0
    _game = None
    _chosenNumber = -1
    
    def __init__(self, game):
        self._game = game
    
    def start(self):
        print("Let's start round {0}!".format(self._game._rounds))
        self.chooseNumber()
        self.startGuessing()
        
    def chooseNumber(self):
        self._chosenNumber = randint(self._game._minNumber, self._game._maxNumber)
        print("I've chosen a number.")
        
    def startGuessing(self):
        print("What is your guess?")
        self._currentNumberOfGuesses = self._currentNumberOfGuesses + 1
        guess = self.getGuess()
        self.processGuess(guess)
            
        
    def getGuess(self):
        guess = input("Make a guess between {0} and {1}: ".format(self._game._minNumber, self._game._maxNumber))
        if guess == "":
            print("I didn't hear you. Speak up please.")
            return self.getGuess()
        elif not guess.isnumeric():
            print("Are you dumb? This is not a number.")
            return self.getGuess()
        guessNum = int(guess)
        if guessNum < self._game._minNumber:
            print("This number is to small")
            return self.getGuess()
        elif guessNum > self._game._maxNumber:
            print("This number is to large")
            return self.getGuess()
        return guessNum
    
    def processGuess(self, value):
        if value == self._chosenNumber:
            print("This is the correct answer.")
            self.processGuessWin()
            return
        if value < self._chosenNumber:
            print("No, this number is smaller then mine.")
        else:
            print("No, this number is larger then mine.")
        self.processGuessLoss()
        
    def processGuessWin(self):
        print("Very well. The victory is yours.")
        self._game._player._points = self._game._player._points + 1
        
    def processGuessLoss(self):
        if self._currentNumberOfGuesses < self._game._maxNumberOfGuesses:
            print("Try again")
            self.startGuessing()
        else:
            print("I am very sorry my dear! You lost.")
            print("The number was {0}".format(self._chosenNumber))
            self._game._npc._points = self._game._npc._points + 1
        

player = Player()
npc = Player()
npc.setName("Old Lady")
game = Game(player, npc, 5, 0, 30)
game.launch()


# In[ ]:





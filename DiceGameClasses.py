#Classes  for Dice Game

import random


class Die:
	def __init__(self, numSides):
		self.numSides  = numSides
		self.value = 1
		
	def roll(self):
		self.value = random.randint(1,self.numSides)
		
	def getValue(self):
		return self.value
		
	def __str__(self):
		return(f"You rolled a {self.value}.")
		
	def __add__(self, val2):
		return self.value + val2.value
		
	def __gt__(self, val2):
		return self.value > val2.value
		
		
class Player:
	def __init__(self, name):
		self.name = name
		self.die1 = Die(6)
		self.die2 = Die(10)
		
			
	
	def rollDice(self):
		self.die1.roll()
		self.die2.roll()
		
		
	def getDiceValue(self):
		return self.die1 + self.die2
		
	def __str__(self):
		return (f"{self.name} {self.getDiceValue()}")
		

class HighTwoGame:
	def __init__(self, player1, player2):
		self.player1 = Player(player1)
		self.player2 = Player(player2)
		self.player1score = 0
		self.player2score = 0
		
	def playOneGame(self):
		self.player1.rollDice()
		self.player2.rollDice()
	
	def playManyGames(self, numGames):
		self.numGames = numGames
		while numGames > 0:
			self.player1.rollDice()
			self.player2.rollDice()
			if self.player1.getDiceValue() > self.player2.getDiceValue():
				self.player1score +=1
				numGames -=1
			elif self.player1.getDiceValue() < self.player2.getDiceValue():
				self.player2score +=1
				numGames -= 1
		
			

			
	
	def __str__(self):
		result = ""
		if self.player1score == 0 and self.player2score == 0:
		
			result += (f"{self.player1.name} rolled a {self.player1.getDiceValue()}\n{self.player2.name} rolled a {self.player2.getDiceValue()}\n")
			if self.player1.getDiceValue() > self.player2.getDiceValue():
				result += (f"{self.player1.name} wins!")
			elif self.player1.getDiceValue() == self.player2.getDiceValue():
				result += ("Tie")
			elif self.player1.getDiceValue() < self.player2.getDiceValue():
				result += (f"{self.player2.name} wins!")
		else: 
			result += (f"the score is {self.player1score} to {self.player2score}\n")
			if self.player1score > self.player2score:
				result += (f"{self.player1.name} wins!")
			elif self.player1score == self.player2score:
				result += ("Tie")
			elif self.player1score < self.player2score:
				result += (f"{self.player2.name} wins!")
			
		return result
'''		
game1 = HighTwoGame("ryker","tyson")
		
		
game1.playOneGame()

print(game1)
'''

"""
Creston Dorothy
11/16/2023

This program...
"""
from DiceGameClasses import Die
from DiceGameClasses import Player
from DiceGameClasses import HighTwoGame

print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
print(game1)

print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
game2.playOneGame()
print(game2)


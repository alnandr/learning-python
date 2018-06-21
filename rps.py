#!/bin/python3
#Rock, Paper, Scissors by Alan Garcia
from random import randint

#Ask the player to pick from rock, paper, or scissors
player = input('Rock (rock), Paper (paper), or Scissors (scissors)?')

print(player, 'vs', end=' ')
# Computer then randomly picks an integer between one and three
chosen = randint(1,3)

# Define integers to equal the computer's selection

if chosen == 1:
  computer = 'rock'
  
elif chosen == 2:
  computer = 'paper'
  
elif chosen == 3:
  computer = 'scissors'
  
print(computer)

# Define rules of the game

if player == computer:
  print('DRAW!')
  
elif player == 'rock' and computer == 'scissors':
  print('Player wins!')
  
elif player == 'rock' and computer == 'paper':
  print('Computer wins!')
  
elif player == 'paper' and computer == 'rock':
  print('Player wins!')
  
elif player == 'paper' and computer == 'scissors':
  print('Computer wins!')
  
elif player == 'scissors' and computer == 'paper':
  print('Player wins!')
  
elif player == 'scissors' and computer == 'rock':
  print('Computer wins!')

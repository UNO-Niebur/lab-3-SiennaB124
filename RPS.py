#RPS.py
#Name: Sienna Bonner
#Date: 2/4/26
#Assignment: Lab 3 RPS
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playAgain = "Y"
  while playAgain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.

    #Randomly choose the computer between 'R', 'P', or 'S'
    Computer = random.choice( ["R", "P", "S"] )
    Player = input("Pick your poison (R, P, S): ")
    #Prompt the user for their RPS selection
    #Determine winner and state what happened to the user
    if Computer == "R":
      print("computer chose rock")
    elif Computer == "P":
      print("computer chose paper")
    else:
      print("computer chose scissors")

    if Player == "R":
      print("Player chose rock")
    elif Player == "P":
      print("Player chose paper")
    else:
      print("Player chose scissors")

    if Player == "R" and Computer == "R":
      print("Tie")
      ties = ties + 1
    if Player == "R" and Computer == "P":
      print("computer wins.")
      losses = losses + 1
    if Player == "R" and Computer =="S":
      print("You win!")
      wins = wins + 1

    if Player == "P" and Computer == "P":
      print("Tie")
      ties = ties + 1
    if Player == "P" and Computer == "S":
      print("computer wins.")
      losses = losses + 1
    if Player == "P" and Computer =="R":
      print("You win!")
      wins = wins + 1

    if Player == "S" and Computer == "S":
      print("Tie")
      ties = ties + 1
    if Player == "S" and Computer == "R":
      print("computer wins.")
      losses = losses + 1
    if Player == "S" and Computer =="P":
      print("You win!")
      wins = wins + 1
    #Ask the user if they would like to play again.
    playAgain = input("Play again? (Y/N): ")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()

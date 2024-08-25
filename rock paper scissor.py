from getpass import getpass as input
print("===EPIC ROCK PAPER SCISSORS BATTLE===")
print()
player1 = input("Player 1, select your move (R, P or S): ")
player2= input("Player 2, select your move (R, P or S): ")
if player1=="R" and player2=="R" or player1=="P" and player2=="P" and player1=="S" and player2=="S":
  print("tie")
elif player1=="R" and player2=="S" or player1=="S" and player2=="P" or player1=="P" and player2=="R":
  print("Player 1 wins")
elif player1=="S" and player2=="R" or player1=="P" and player2=="S" or player1=="R" and player2=="P":
  print("Player 1 wins")
else:
  print("Invalid move")
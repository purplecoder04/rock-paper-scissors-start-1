rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
play=[rock, paper, scissors]
com_play=random.randint(0,2)


print("welcome to Rock, Paper, Scissors")
answer=int(input("Choice 0=Rock,1=Paper, Or 2=Scissors \n"))
if answer > 2:
  print("try again wrong number")
else:
  print(play[answer])
  print(com_play)
  print(play[com_play])
  if com_play == answer:
    print("it's a tie")
  elif com_play == 0 and answer == 2:
    print("You lose")
  elif answer == 0 and com_play == 2:
    print("You won")
  elif com_play == 2 and answer == 1:
    print("you lose")
  elif answer == 2 and  com_play == 1:
    print("you won")
  elif com_play == 1 and answer == 0:
    print("you lose")
  elif com_play == 0 and answer == 1:
    print("you won")
    
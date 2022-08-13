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

#Write your code below this line 👇
import random
list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print (list[user_choice])
comp_choice = random.randint(0,2)
print("Computer chose:")
print (list[comp_choice])
if (user_choice == 0 and comp_choice == 1) or (user_choice == 2 and comp_choice == 0) or (user_choice == 1 and comp_choice == 2):
  print("You loose!")
elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
  print("You win!")
else:
  print("Dead heat. Try again.")

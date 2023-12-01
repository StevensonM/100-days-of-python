import random

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


print("What do you choose?")
print("Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

num = int(input())

random_num = random.randint(1, 3)

if num == 0:
    print(rock)
elif num == 1:
    print(paper)
elif num == 2:
    print(scissors)

print("Computer chose:")

if random_num == 0:
    print(rock)
elif random_num == 1:
    print(paper)
elif random_num == 2:
    print(scissors)

if num >= 3 or num < 0:
    print("You typed an invalid number, you lose!")
elif num == 0 and random_num == 2:
    print("You win!")
elif random_num == 0 and num == 2:
    print("You lose")
elif random_num > num:
    print("You lose")
elif num > random_num:
    print("You win!")
elif random_num == num:
    print("It's a draw")

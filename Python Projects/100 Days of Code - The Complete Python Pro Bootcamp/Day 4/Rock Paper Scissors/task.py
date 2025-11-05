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

pick_r_p_s = ["Rock", "Paper", "scissors"]
computer_choice = random.choice(pick_r_p_s)

choice_0 = pick_r_p_s[0]
choice_1 = pick_r_p_s[1]
choice_2 = pick_r_p_s[2]

my_choice = input(" What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. ")
if my_choice == "0":
    if computer_choice == choice_0:
       print(rock)
       print("Computer chose: ")
       print(rock)
       print("its a draw!")
    elif computer_choice == choice_1:
       print(rock)
       print("Computer chose: ")
       print(paper)
       print("Yoo loose!")
    elif computer_choice == choice_2:
       print(rock)
       print("Computer chose: ")
       print(scissors)
       print("You win!")
elif my_choice == "1":
    if computer_choice == choice_1:
       print(paper)
       print("Computer chose: ")
       print(paper)
       print("its a draw!")
    elif computer_choice == choice_0:
        print(paper)
        print("Computer chose: ")
        print(rock)
        print("You win!")
    elif computer_choice == choice_2:
        print(paper)
        print("Computer chose: ")
        print(scissors)
        print("You loose!")
elif my_choice == "2":
        if computer_choice == choice_2:
            print(scissors)
            print("Computer chose: ")
            print(scissors)
            print("It's a draw!")
        elif computer_choice == choice_0:
            print(scissors)
            print("Computer chose: ")
            print(rock)
            print("You loose!")
        else:
            if computer_choice == choice_1:
                print(scissors)
                print("Computer chose: ")
                print(paper)
                print("You Win!")
else:
    print("Careful, you typed an invalid response. You loose!")

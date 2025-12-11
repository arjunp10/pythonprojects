import random
print("welcome to rock, paper, scissors!")
user_score = 0
compiuter_score = 0
rounds = int(input("How many rounds do you want to play? "))
for round in range(rounds):
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("The computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win this round!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win this round!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        compiuter_score += 1
print("Final Scores - You:", user_score, "Computer:", compiuter_score)
if user_score > compiuter_score:
    print("Congratulations! You won the game!")
elif user_score < compiuter_score:
    print("Computer wins the game! Better luck next time.")
else:
    print("The game is a tie!")
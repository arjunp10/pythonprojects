import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Please enter a valid number.")

max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)

while max(player_scores) < max_score:

    for i in range(players):
        print(f"Player {i + 1}'s turn:")
        print("Your current score is:", player_scores[i])
        current_score = 0
        while True:
            should_roll = input("Do you want to roll the dice? (yes/no) ")
            if should_roll.lower() != "yes":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1! No points this turn.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}!")
            print("Your turn score is:", current_score)

        player_scores[i] += current_score
        print("Your total score is:", player_scores[i])
winner = player_scores.index(max(player_scores)) + 1
print(f"Player {winner} wins with a score of {max(player_scores)}!")

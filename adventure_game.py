user = input("what is your name? ")
print("welcome" , user, "to this adventure!")
ask1 = input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()
if ask1 == "left":
    ask2 = input("you come to a river, you can walk around it or swim across? type walk to walk around and swim to swim across: ").lower()
    if ask2 == "swim":
        print("you swam across and were eaten by an alligator. game over!")
    elif ask2 == "walk":
        print("you walked for many miles, ran out of water and lost the game")
    else:
        print("not a valid option. you lose")
elif ask1 == "right":
    ask3 = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()
    if ask3 == "back":
        print("you go back and lose")
    elif ask3 == "cross":
        print("you crossed the bridge and found a treasure chest full of gold! you win!")
    else:
        print("not a valid option. you lose")
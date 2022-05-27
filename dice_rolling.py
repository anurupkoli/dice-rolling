import random

player_score = 0
comp_score = 0

print("Welcome my Friend, you have to score 50 points before computer does it to WIN!!")

while True:

    if comp_score >= 50 or player_score >= 50:
        break

    dice1 = (input("Do you want to roll the dice?...click '(y/n)': "))
    dice = dice1.lower()
    if dice == "y":
        # Player :
        dice_no = random.randint(1, 6)
        print("Your turn: ")
        print(f"Your Dice = {dice_no}")
        player_score += dice_no
        print(f"Your Score = {player_score}")
        # Computer :
        print("computer's turn: ")
        comp = random.randint(1, 6)
        print(f"Computer's Dice = {comp}")
        comp_score += comp
        print(f"Computer's score = {comp_score}")

    elif dice == "n":
        break
    elif dice == "":
        print("Please enter valid alphabet '(y/n)'")
        False
    else:
        print("Please enter valid alphabet '(y/n)'")
        False

if comp_score >= 50:
    print("Computer won!! Better  luck next time :)")

elif player_score >= 50:
    print("Congratulations.You won!!")

print("Thankyou for playing :)")

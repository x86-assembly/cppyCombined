import random

print("Welcome to this game")
chosen_range = int(input("up to what number do you want to guess?\n> "))

def game():
    number = random.randint(1,chosen_range)
    while True:
        guess = int(input("what number do you guess?\n> "))
        if guess==number:
            print("You won!")
            return
        if guess>number:
            print("Too large!")
        else:
            print("Too small!")
            
while True:
    game()
    if(input("Do you want to play again? (y/n)\n> ") == "n"):
        break
import random

def number_guessing_game():
    random_number = random.randint(1,100)
    current_chance = 0
    max_chances = 5
    print(f"Welcome to number guessing game, you get {max_chances} chances to guess the number")


    while current_chance < max_chances:
        try:
            guess = int(input(f"""
                            You have {max_chances - current_chance} chances left
                            
                            Select a number from 1 to 100"""))

            if guess == random_number:
                print(f"""
                            YAYYYY!
                            YOU WON 
                            Thw number is {random_number}
                        """)
                return
            elif guess < random_number:
                print("guess was too low, try going higher")
            elif guess > random_number:
                print("guess was too high, try going a bit lower")

            current_chance += 1

        except ValueError:
            print("please enter a vlid number")

    print(f"GAME OVER the secret number was {random_number}")

if __name__ == "__main__":
    number_guessing_game()
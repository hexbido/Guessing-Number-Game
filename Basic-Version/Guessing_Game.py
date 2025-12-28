import random

# --------------------------------[ Configuration ]-----------------------------------

attempts_list = []

def show_score():
    """ Displays the current high score (minimum attempts). """
    if not attempts_list:
        print("There Is No High Score, Start Playing!")
    else:
        print(f"The Current High Score Is {min(attempts_list)} Attempts.")

# --------------------------------[ Game Setup ]-----------------------------------

print("Welcome To The Guessing Game!")

# Keep User's Original Prompt
player_name = input("What's Your Name? ").strip().capitalize()
ask_player = input(f"Hello {player_name}! Do You Want To Play The Guessing? (yes/no): ").strip().lower()

if ask_player != "yes":
    print("That's Amazing, Thank You!")
    exit()
else:
    show_score()

print("We Are Going To Pick A Number Between 1 And 10, And You Have To Guess It!")

# --------------------------------[ Main Game Loop ]-----------------------------------

while ask_player == "yes":
    
    # Generate Random Number
    random_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            # Keep User's Original Prompt
            guess = int(input("Pick A Number Between 1 And 10: "))
            
            # Logic Validation
            if guess < 1 or guess > 10:
                raise ValueError("Please Guess A Number Within The Given Range")
            
            attempts += 1

            # Check The Guess
            if guess == random_number:
                print(f"Nice {player_name}, You Got It!")
                print(f"You Guessed The Number '{random_number}' Correctly! It Took You {attempts} Attempts!")
                
                attempts_list.append(attempts)
                
                # Ask To Play Again
                ask_player = input("Would You Like To Play Again (yes/no): ").strip().lower()
                
                if ask_player == "no":
                    print("It's Okay, See You Next Time.")
                    # Exit The Inner Loop To Reach The Outer Loop Check
                    break 
                else:
                    # Reset Logic For New Game
                    show_score()
                    break # Break Inner Loop To Restart Outer Loop

            elif guess > random_number:
                print("Hint: It's Lower!")
            else:
                print("Hint: It's Higher!")

        except ValueError as error:
            print(error)
            
    # Condition To Break The Main Loop If User Said 'no'
    if ask_player == "no":
        break
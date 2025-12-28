import random, math, os, time

class GuessGame:
    def __init__(self):
        # --------------------[ Configuration ]--------------------
        self.score_file = "highscore.txt"
        self.player_name = ""
        # Keep User's Original Level Definitions
        self.levels = {
            "1": {"name": "Easy",   "range": 10,   "meaning": " | Choose Between 1 and 10",   "tries": 10},
            "2": {"name": "Medium", "range": 100,  "meaning": " | Choose Between 1 and 100",  "tries": 15},
            "3": {"name": "Hard",   "range": 1000, "meaning": " | Choose Between 1 and 1000", "tries": 20}
        }

    # --------------------[ Helper Functions ]--------------------

    def manage_score(self, new_score=None):
        """ Handles reading and writing high scores to file. """
        try:
            current = int(open(self.score_file).read())
        except (FileNotFoundError, ValueError):
            current = 999
        
        if new_score and new_score < current:
            with open(self.score_file, "w") as f: f.write(str(new_score))
            print(f"\nSystem | New Record By {self.player_name}: {new_score} Attempts!")
            return new_score
            
        return current if current != 999 else "None"

    def get_hint(self, n):
        """ Generates mathematical hints based on the number properties. """
        props = [f"Divisible By {i}" for i in [2, 3, 5] if n % i == 0]
        
        # Check For Prime
        if n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
            props.append("Hint For You : Prime Number")
            
        return random.choice(props) if props else "No Distinct Properties"

    # --------------------[ Game Modes ]--------------------

    def play_ai(self, limit):
        """ AI Solver using Binary Search. """
        low, high, attempts = 1, limit, 0
        
        # Keep User's Original Prompt
        print(f"\nAI Mode | Thinking Of A Number Between 1-{limit}...")
        input(">> Press Enter When You Ready...")
        
        while low <= high:
            attempts += 1
            guess = (low + high) // 2
            time.sleep(0.5)
            
            print(f"\nAI Guess : Is It {guess}?")
            # Keep User's Original Prompt
            fb = input(">> (H)igh, (L)ow, (C)orrect? ").lower().strip()
            
            if fb == 'c': 
                print(f"\nResult | AI Won In {attempts} Attempts.")
                return
            elif fb == 'h': low = guess + 1
            elif fb == 'l': high = guess - 1
            else: attempts -= 1 # Invalid Input Correction
            
        print("\nError!! | Calculation Error, Please Check Your Responses.")

    def play_user(self, config):
        """ User Playing vs PC. """
        limit, max_tries = config["range"], config["tries"]
        secret, attempts = random.randint(1, limit), 0
        
        print(f"\nGame Start | Good Luck {self.player_name}! | You Will Choose Between: 1-{limit}")

        while attempts < max_tries:
            try:
                # Keep User's Original Prompt
                guess = int(input(f">> Attempt {attempts + 1}/{max_tries}: "))
                attempts += 1
                
                if guess == secret:
                    print(f"\nVictory | Your Choice Is Correct! Well Done {self.player_name}.")
                    self.manage_score(attempts)
                    return
                
                # Hints
                print(">> Hint For You: Go Higher" if guess < secret else ">> Hint For You: Go Lower")
                
                if attempts == max_tries // 2: 
                    print(f">> Smart Hint: {self.get_hint(secret)}")
                    
            except ValueError: 
                pass # Ignore non-integer inputs without crashing
                
        print(f"\nYour Defeat ): | Your Attempts Have Ended | The Correct Number Was {secret}.")

    # --------------------[ Main Entry Point ]--------------------

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Keep User's Original Header Design
        print(f"{'='*50}\n   Guessing Edition By Bido   |   Best Score: {self.manage_score()}\n{'='*50}")
        print("\nWelcome To The Guessing Game | Here You Can Play Against The PC Or Let The AI Solve It!")
        
        self.player_name = input(">> Enter Player Name: ").strip().title() or "Guest"
        
        while True:
            print(f"\nMenu | User Name: {self.player_name}")
            # Keep User's Original Menu Options
            choice = input("Select Mode | 1: Play Game Vs PC | 2: AI Solver | 3: Exit\n>> Select: ").strip()
            
            if choice == '3': 
                print(f"\nSystem Exiting | See You Again, {self.player_name}.")
                break
                
            if choice not in ['1', '2']: 
                continue

            print("\nLevels | Choose Difficulty:")
            for k, v in self.levels.items(): 
                print(f" {k}: {v['name']} (1-{v['range']} {v['meaning']})")
            
            lvl = input(">> Select Level: ").strip()
            
            if lvl in self.levels:
                if choice == '1': self.play_user(self.levels[lvl])
                else: self.play_ai(self.levels[lvl]["range"])
            else: 
                print("Error!! : Invalid Level | Please Select 1, 2, or 3.")

if __name__ == "__main__":
    GuessGame().start()
import random
def guessing_game():
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
           
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()

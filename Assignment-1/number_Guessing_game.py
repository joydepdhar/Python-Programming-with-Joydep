import random

def guess_game():
    number=random.randint(1,100)
    print(number)
    count=0
    while True:
        try:
            a=int(input("Enter Your Guess: "))
            count+=1 
            if number==a:
                print(f"Congratulations! You've guessed the number in {count} attempts.")
                break
            elif a>number:
                print("too high!")
            elif a<number:
                print("too low!")
        except ValueError:
            print("Invalid Input")
          
def main():
    print("Welcome to Guessing Game")
    print("You have to guess a number between 1 and 100")
    guess_game()
if __name__ == "__main__":
    main()
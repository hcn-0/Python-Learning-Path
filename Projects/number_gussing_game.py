import random


def main():
    print("Wellcome to number guessing game!")
    print("I'm thinking a number between 1 to 100. Try to guess it.")
    random_number = random.randint(1,100)
    count = 0
    while True:
        number = guess_number()
        count = count + 1
        if number == random_number:
            print(f"You got it! You guessed in {count} tries.")
            break;
        elif number < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    play = input("Wanna play again? y/n: ")
    if play == "y":
        main()
        


def guess_number():
    n = int(input("Enter you guess: "))
    return n
    
main()
    


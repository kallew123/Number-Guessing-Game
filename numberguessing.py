import random

secret_easy = random.randint(1, 50)
secret_medium = random.randint(1, 100)
secret_hard = random.randint(1, 200)


def easy():
    for i in range(5):
        try:
            print(f"\nAttempt {i + 1}")
            num = int(input("Enter your guess: "))

            if num == secret_easy:
                print("Congratulations, you got it!")
                break
            else:
                if i < 4:
                    print("Wrong! Try again.")
                    if num < secret_easy:
                        print("A bit higher!")
                    else:
                        print("A bit lower!")
                else:
                    print("You lost! No attempts left.")

        except ValueError:
            print("That is not a number!")


def medium():
    for i in range(5):
        try:
            print(f"\nAttempt {i + 1}")
            num = int(input("Enter your guess: "))

            if num == secret_medium:
                print("Congratulations, you got it!")
                break
            else:
                if i < 4:
                    print("Wrong! Try again.")
                    if num < secret_medium:
                        print("A bit higher!")
                    else:
                        print("A bit lower!")
                else:
                    print("You lost! No attempts left.")

        except ValueError:
            print("That is not a number!")


def hard():
    for i in range(5):
        try:
            print(f"\nAttempt {i + 1}")
            num = int(input("Enter your guess: "))

            if num == secret_hard:
                print("Congratulations, you got it!")
                break
            else:
                if i < 4:
                    print("Wrong! Try again.")
                    if num < secret_hard:
                        print("A bit higher!")
                    else:
                        print("A bit lower!")
                else:
                    print("You lost! No attempts left.")

        except ValueError:
            print("That is not a number!")


print("Guess the secret number!\n")
print("You have 5 attempts to guess the number.\n")

while True:
    print("Choose the difficulty level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)\n")

    try:
        choice = int(input("Level: "))

        if choice == 1:
            easy()
            break
        elif choice == 2:
            medium()
            break
        elif choice == 3:
            hard()
            break
        else:
            print("Invalid!")

    except ValueError:
        print("Enter a number from 1 to 3!")

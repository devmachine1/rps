import random;

print("Welcome to my Rock, Paper, Scissors Game!")

randint = random.randint(1, 3)
name = input("Name: ")
inputNum = int(input("[1] Rock, [2] Paper, [3] Scissors: "))

match inputNum:
    case 1:
        print("Rock")

    case 2:
        print("Paper")

    case 3:
        print("Scissors")

match randint:
    case 1:
        print("Rock")

    case 2:
        print("Paper")

    case 3:
        print("Scissors")

if (inputNum == randint):
        print("Draw!")

elif inputNum == 1 and randint == 2:
    print("Bot Wins!")

elif inputNum == 1 and randint == 3:
    print(name + " Wins!")

elif inputNum == 2 and randint == 1:
    print(name + " Wins!")

elif inputNum == 2 and randint == 3:
    print("Bot Wins!")

elif inputNum == 3 and randint == 1:
    print("Bot Wins!")

elif inputNum == 3 and randint == 2:
    print(name + " Wins!")

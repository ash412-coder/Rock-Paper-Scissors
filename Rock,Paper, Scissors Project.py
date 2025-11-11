#Rock,Paper, Scissors Project

#Problem – Rock, Paper, Scissors (Computer vs. Player)
#Make a program where the computer randomly chooses rock, paper, or scissors. Ask the user for their
#choice and decide who wins. Let the game run in a loop until the user types 'quit'. Print a scoreboard
#showing wins, losses, and ties.
#Goals: Combine input, conditionals, random numbers, and loops.
import random

computer_option = ["Rock", "Paper", "Scissors"]
wins = 0
losses = 0
tie = 0

choice = input("Pick Rock, Paper or Scissors (or type 'quit' to stop): ").lower()

while choice != "quit":
    computer_pick = random.choice(computer_option).lower()
    print("\nComputer picked:", computer_pick)

   
    if choice == "rock":
        if computer_pick == "rock":
            tie += 1
            print("You Entered a Tie Try Again!")
        elif computer_pick == "paper":
            losses += 1
            print("The Computer Wins, Try Again!")
        elif computer_pick == "scissors":
            wins += 1
            print("You Win!")

    
    elif choice == "paper":
        if computer_pick == "paper":
            tie += 1
            print("You Entered a Tie Try Again!")
        elif computer_pick == "scissors":
            losses += 1
            print("The Computer Wins, Try Again!")
        elif computer_pick == "rock":
            wins += 1
            print("You Win, Good Job!")

    
    elif choice == "scissors":
        if computer_pick == "scissors":
            tie += 1
            print("You Entered a Tie Try Again!")
        elif computer_pick == "rock":
            losses += 1
            print("The Computer Wins, Try Again!")
        elif computer_pick == "paper":
            wins += 1
            print("You Win, Good Job!")

    
    else:
        print("Invalid choice. Please type Rock, Paper, or Scissors.")

    print("\nScoreboard -> Wins:", wins, "Losses:", losses, "Ties:", tie)
    choice = input("\nPick Rock, Paper or Scissors (or type 'quit' to stop): ").lower()




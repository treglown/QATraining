import random
def rock_paper_scissors():
    user_turn = input("Pick an action: rock, paper, scissors")

    possible_moves = ["rock", "paper", "scissors"]
    computer_moves = random.choice(possible_moves)

    print(f"Your move is {user_turn}, computer move is {computer_moves}.")


    while True: 
        user_turn = input("Pick an action: rock, paper, scissors")

        possible_moves = ["rock", "paper", "scissors"]
        computer_moves = random.choice(possible_moves)

        print(f"Your move is {user_turn}, computer move is {computer_moves}.")
        if user_turn == computer_moves:
            print(f"Both moves are the same, DRAW!")
            try_again = input("Try again? (yes or no)")
            if try_again.lower() != "yes":
                break

        elif user_turn == "rock":
            if computer_moves == "scissors":
                print("Rock beats scissors! You have won!")
            else:
                print("Paper beats rock! You lose!")
        elif user_turn == "paper":
            if computer_moves == "rock":
                print("Paper beats rock, You win!")
            else:
                print("Scissors beats paper. You lose!")
        elif user_turn == "scissors":
            if computer_moves == "paper":
                print("Scissors beats paper. You Win")
            else:
                print("Rock beats scissors. You lose!")
        else:
            print("Unrecognized input, try again!")

        try_again = input("Try again? (yes or no)")
        if try_again.lower() != "yes":
            break

number_of_rounds = 0
user_wins = 0
computer_wins = 0
try_again = 'yes'

while try_again == 'yes':
    number_of_rounds += 1
    result = rock_paper_scissors()

    if result == "You win!":
        user_wins +=1
    elif result == "You lose!":
        computer_wins += 1
    else:
        print("END - The game is a draw!") 
print(user_wins)
print(computer_wins)
print(number_of_rounds)




# while try_again == 'yes':
#     number_of_rounds += 1
#     result = rock_paper_scissors()

#     if rock_paper_scissors == ("Scissors beats paper. You Win", "Rock beats scissors! You have won!", "Paper beats rock, You win!"):
#         user_wins += 1
#     elif computer_wins == ("Rock beats scissors. You lose!", "Scissors beats paper. You lose!","Paper beats rock! You lose!" ):
#         computer_wins += 1
#     elif number_of_rounds == 3:
#         rock_paper_scissors == "Game ended check your scores!"
#         print(user_wins)
#         print(computer_wins)
#         print(number_of_rounds)
#     break



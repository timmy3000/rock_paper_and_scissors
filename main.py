import random

possible_actions = ['R', 'P', 'S']
player_score = 0
cpu_score = 0

while True:

    # getting the player's choice
    player_action = input("Enter your choice (Rock[R], Paper[P], Scissors[S]): ").upper()

    # randomizing the cpu's choice
    cpu_action = random.choice(possible_actions)

    print(f"\nPlayer ({player_action}) : CPU ({cpu_action})\n")

    if(not(player_action in possible_actions)):
        print("Invalid entry, Please try again.\n")
        continue


    if(player_action == cpu_action):
        player_score += 1
        cpu_score += 1

        print(f"Both players selected {player_action}. It's a tie!\n")
        print(f"You: {player_score}")
        print(f"CPU: {cpu_score}\n")

    elif(player_action == "R"):
        if(cpu_action == "S"):
            player_score += 1

            print("Rock beats Scissors! You win!\n")
            print(f"You: {player_score}")
            print(f"CPU: {cpu_score}\n")

        else:
            cpu_score += 1

            print("Paper beats rock! You lose.\n")
            print(f"You: {player_score}")
            print(f"CPU: {cpu_score}\n")

    elif(player_action == "P"):
        if(cpu_action == "R"):
            player_score += 1

            print("Paper beats rock! You win!\n")
            print(f"You: {player_score}")
            print(f"CPU: {cpu_score}\n")

        else:
            cpu_score += 1

            print("Scissors beats paper! You lose.\n")
            print(f"You: {player_score}")
            print(f"CPU: {cpu_score}\n")

    elif(player_action == "S"):
        if cpu_action == "P":
            player_score += 1

            print("Scissors beats paper! You win!\n")
            print(f"You: {player_score}")
            print(f"CPU: {cpu_score}\n")

        else:
            cpu_score += 1

            print("Rock beats scissors! You lose.\n")
            print(f"You: {player_score}")
            print(f"CPU: {cpu_score}\n")

    else:
        print("Invalid entry.\n")


    play_again = input("Play again? (y/n): ")

    if play_again.lower() != "y":
        break
        
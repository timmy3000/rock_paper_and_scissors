import random

possible_actions = ['R', 'P', 'S']

titles = {'R': "Rock", 'P': "Paper", 'S': "Scissors"}

while True:

    # getting the player's choice
    player_action = input("Enter your choice (Rock[R], Paper[P], Scissors[S]): ").upper()

    # randomizing the cpu's choice
    cpu_action = random.choice(possible_actions)


    if(not(player_action in possible_actions)):
        print("Invalid entry, Please try again.\n")
        continue

        
    print(f"\nPlayer ({titles[player_action]}) : CPU ({titles[cpu_action]})\n")


    if(player_action == cpu_action):
        print(f"Both players selected {player_action}. It's a tie!\n")

    elif(player_action == "R"):
        if(cpu_action == "S"):
            print("Rock beats Scissors! You win!\n")
            break
        else:
            print("Paper beats rock! You lose.\n")
            break

    elif(player_action == "P"):
        if(cpu_action == "R"):
            print("Paper beats rock! You win!\n")
            break
        else:
            print("Scissors beats paper! You lose.\n")
            break

    elif(player_action == "S"):
        if(cpu_action == "P"):
            print("Scissors beats paper! You win!\n")
            break
        else:
            print("Rock beats scissors! You lose.\n")
            break

    else:
        print("Invalid entry.\n")

        

import random


print("Welcome to Rock Paper Scissors!")
print("Make a throw")

choices = ["R" , "P", "S"]
computer_input = random.choice(choices)
player = False
    

while player == False:
    player_input = input('"R", "P" or "S"?').capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player_input == computer_input:
        print(f"\nPlayer ({player_input}): CPU ({computer_input})")
        print("Tie!")
    elif player_input == "R":
        if computer_input == "S":
            print(f"\nPlayer ({player_input}): CPU ({computer_input})")
            print("Computer wins!")
        else:
            print("You win! Rock smashes Scissors.")
                
    elif player_input == "P":
        if computer_input == "R":
            print(f"\nPlayer ({player_input}): CPU ({computer_input})")
            print("Computer wins!")
        else:
            print("You win! Paper covers Rock.")
               
    elif player_input == "S":
        if computer_input == "P":
            print(f"\nPlayer ({player_input}): CPU ({computer_input})")
            print("Computer wins!")
        else:
            print("You win! Scissors cuts Paper.")
                
    elif player_input != player_input:
        if computer_input != computer_input:
            print("That's not a valid play. Enter a valid action!")
            #player was set to True, but we want it to be False so the loop continues
       
    play_again = input("Play again? y/n: ").lower()
    if play_again == "y":
        pass
    elif play_again == "n":
        break
    else:
        break
print ("Thanks for playing, GOODBYE")  
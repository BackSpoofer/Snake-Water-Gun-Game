#Snake Water Gun Game
#Designed By -- Manoj Kumar Dahiya


import random
bot1 = ["Snake", "Water", "Gun"]
player_wins = 0
bot_wins = 0
game_draws = 0

print("*********************************************************************************************")
print("||        :::::Welcome to the Traditional Snake Water Gun Game in Modern Way:::::          ||")
print("||                                                                                         ||")
print("||                   This is a bot playing with you; So, be smarter                        ||")
print("||                                                                                         ||")
print("||                                                     Credits        --Manoj Kumar Dahiya ||")
print("*********************************************************************************************")


print("Instructions for the game--")
print("                             1. Choose any of the three options below")
print("                             1. There are 10 rounds of Game")
print("                             2. After the end of game Your Score will be presented")



print("---------------------------------------------------------------------------------------------")

for i in range(10):

    bot = random.choice(bot1)

    print("\n---> Enter Your Choice: 1. Snake")
    print("                        2. Water")
    print("                        3. Gun")
    player = input()

    if player == "1" or player == "snake" or player == "Snake":
        if bot == "Snake":
            print("Computer Guessed: " + bot)
            print("Its Draw ---- Phew!!! That was too Close....")
            game_draws += 1
        elif bot == "Water":
            print("Computer Guessed: " + bot)
            print("---Your Snake drank water---")
            print("<<< Congratulations >>> Yow Win!!!")
            player_wins += 1
        elif bot == "Gun":
            print("Computer Guessed: " + bot)
            print("---Your Snake was Shot and Killed by Gun---")
            print("Sorry! You Lose :(")
            bot_wins += 1

    elif player == "2" or player == "water" or player == "Water":
        if bot == "Water":
            print("Computer Guessed: " + bot)
            print("Its Draw ---- Phew!!!  That was too Close....")
            game_draws += 1
        elif bot == "Gun":
            print("Computer Guessed: " + bot)
            print("---Gun got Damaged by your Water---")
            print("<<< Congratulations >>> Yow Win!!!")
            player_wins += 1
        elif bot == "Snake":
            print("Computer Guessed: " + bot)
            print("---The Snake Drank all of your Water---")
            print("Sorry! You Lose :(")
            bot_wins += 1

    elif player == "3" or player == "gun" or player == "Gun":
        if bot == "Gun":
            print("Computer Guessed: " + bot)
            print("Its Draw ---- Phew!!!  That was too Close....")
            game_draws += 1
        elif bot == "Snake":
            print("Computer Guessed: " + bot)
            print("---You Shot & Killed the Snake by Gun---")
            print("<<< Congratulations >>> Yow Win!!!")
            player_wins += 1
        elif bot == "Water":
            print("Computer Guessed: " + bot)
            print("---Your Gun got Damaged by Water---")
            print("Sorry! You Lose :(")
            bot_wins += 1

    else:
        print("Invalid Option: ")
        continue

print("\n\n\n\n*********************************************************************************************")
print("     ::::Your Winning Count:" + str(player_wins) + "::::")
print("     ::::Computer      Wins:" + str(bot_wins) + "::::")

if player_wins > bot_wins:
    print("<><><><>Conclusion::::::------- Victory by", player_wins - bot_wins, " -------<><><><>")
elif player_wins < bot_wins:
    print("<><><><>Conclusion::::::------- Defeat  by", bot_wins - player_wins, " -------<><><><>")
else:
    print("<><><><>Conclusion::::::------- It's Draw -------<><><><>")

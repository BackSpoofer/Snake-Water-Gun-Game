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

for i in range(10):

    bot = random.choice(bot1)

    print("Enter Your Choice: 1. Snake")
    print("                   2. Water")
    print("                   3. Gun")
    player = input()

    if player == "1" or player == "snake" or player == "Snake":
        if bot == "Snake":
            print("Its Draw ---- Phew!!!  That was too Close....")
            game_draws += 1
        elif bot == "Water":
            print("<<< Congratulations >>> Yow Win!!!")
            player_wins += 1
        elif bot == "Gun":
            print("Sorry! You Lose :(")
            bot_wins += 1

    elif player == "2" or player == "water" or player == "Water":
        if bot == "Water":
            print("Its Draw ---- Phew!!!  That was too Close....")
            game_draws += 1
        elif bot == "Gun":
            print("<<< Congratulations >>> Yow Win!!!")
            player_wins += 1
        elif bot == "Snake":
            print("Sorry! You Lose :(")
            bot_wins += 1

    elif player == "3" or player == "gun" or player == "Gun":
        if bot == "Gun":
            print("Its Draw ---- Phew!!!  That was too Close....")
            game_draws += 1
        elif bot == "Snake":
            print("<<< Congratulations >>> Yow Win!!!")
            player_wins += 1
        elif bot == "Water":
            print("Sorry! You Lose :(")
            bot_wins += 1

    else:
        print("Invalid Option: ")
        continue


print("     ::::Your Winning Count:" + str(player_wins) + "::::")
print("     ::::Computer      Wins:" + str(bot_wins) + "::::")

if player_wins > bot_wins:
    print("<><><><>Conclusion::::::------- Victory by", player_wins - bot_wins, " -------<><><><>")
elif player_wins < bot_wins:
    print("<><><><>Conclusion::::::------- Defeat  by", bot_wins - player_wins, " -------<><><><>")
else:
    print("<><><><>Conclusion::::::------- It's Draw -------<><><><>")

print("This is a game that starts with 0 and each player adds a number between 1 and 10")
print("the first player who reaches 100 wins the game.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Game mode
game=0
gameMode=int(input("Press (1) for multiplayer or press (2) to play with computer: "))
if gameMode!=1 and gameMode!=2:
    while gameMode!=1 and gameMode!=2:
        gameMode=int(input("Press 1 or 2 only: "))

# Multi player game
if gameMode==1:
    p1 = input("Player1 enter your name: ")
    p2 = input("Player2 enter your name: ")
    print("## Lets start the game ##")

    while game<100:
        # Player1 turn
        while True:
            try:
                player1 = int(input(p1 + " enter your number: "))
                if player1 < 1 or player1 > 10:
                    while player1 < 1 or player1 > 10:
                        player1 = int(input(p1 + " enter a number between 1 and 10 only: "))
                break
            except:
                print('Invalid input enter a number between 1 and 10 only !')

        game+=player1
        while game>100:
            game-=player1
            print(p1+ " you exceeded 100 !")
            player1 = int(input(p1 + " enter a number only to reach 100: "))
            game+=player1
        print("Total=",game)
        if game==100:
            print(p1+ " win !")
            playAgain=input("To play again press y, to exit press n")
            if playAgain!='y' and playAgain!='n':
                while playAgain!='y' and playAgain!='n':
                    playAgain = input("To play again press y, to exit press n")
            if playAgain=="y":
                game=0
                continue
            elif playAgain=="n":
                break

        # Player2 turn
        if game<100:
            while True:
                try:
                    player2 = int(input(p2 + " enter your number: "))
                    if player2 < 1 or player2 > 10:
                        while player2 < 1 or player2 > 10:
                            player1 = int(input(p1 + " enter a number between 1 and 10 only: "))
                    break
                except:
                    print('Invalid input enter a number between 1 and 10 only !')
        game+=player2
        while game>100:
            game -= player2
            print(p2 + " you exceeded 100 !")
            player2 = int(input(p2 + " enter a number only to reach 100: "))
            game+=player2
        print("Total=", game)
        if game==100:
            print(p2+ " win !")
            playAgain = input("To play again press y, to exit press n")
            if playAgain!='y' and playAgain!='n':
                while playAgain!='y' and playAgain!='n':
                    playAgain = input("To play again press y, to exit press n")
            if playAgain == "y":
                game = 0
                continue
            elif playAgain == "n":
                break

#################################################################################################

#play with computer:
if gameMode==2:
    p1=input("Enter your name please: ")
    print("## Lets start the game ##")

    while game<100:
        # Player1 turn
        while True:
            try:
                player1 = int(input(p1 + " enter your number: "))
                if player1 < 1 or player1 > 10:
                    while player1 < 1 or player1 > 10:
                        player1 = int(input(p1 + " enter a number between 1 and 10 only: "))
                break
            except:
                print('Invalid input enter a number between 1 and 10 only !')
        game+=player1
        while game>100:
            game -= player1
            print(p1+ " you exceeded 100 !")
            player1 = int(input(p1 + " enter a number only to reach 100: "))
            game+=player1
        print("Total=",game)
        if game==100:
            print(p1+ " win !")
            playAgain = input("To play again press y, to exit press n")
            if playAgain!='y' and playAgain!='n':
                while playAgain!='y' and playAgain!='n':
                    playAgain = input("To play again press y, to exit press n")
            if playAgain == "y":
                game = 0
                continue
            elif playAgain == "n":
                break

        # Computer turn
        if game<100:
            import random
            computer=random.randint(1,10)
            if 79<game<88:
                computer=89-game
            if 90<game<100:
                computer=100-game
            print("Computer entered (",computer,")")
        game+=computer
        print("Total=", game)
        if game==100:
            print( "Computer win !")
            playAgain = input("To play again press y, to exit press n")
            if playAgain!='y' and playAgain!='n':
                while playAgain!='y' and playAgain!='n':
                    playAgain = input("To play again press y, to exit press n")
            if playAgain == "y":
                game = 0
                continue
            elif playAgain == "n":
                break






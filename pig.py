import random

winning_points = 50

def roll_dice():
    n = random.randint(1, 6)
    return n

def get_num_players():
    while True:
        num = input("How many players are playing? (2-4) ")
        if num.isdigit():
            num = int(num)
            if 2 <= num <= 4:
                break
            else:
                print("Number must be between 2-4!")
        else:
            print("Input must be a number!")

    return num

players = get_num_players()

player_scores = [0 for _ in range(players)]

def main():
    while max(player_scores) < winning_points:
        for player in range(players):
            print(f"Player #{player+1} turn:")
            print(f"Your curent score is {player_scores[player]}.")
            while True:
                answer = input("Would you like to roll? (y/n) ").lower()
                print()
                if answer == "y":
                    roll = roll_dice() 
                    print(f"You got a: {roll}")
                    if roll != 1:
                        player_scores[player] += roll  
                        print(f"Your score is {player_scores[player]}.\n")
                    else:
                        player_scores[player] = 0
                        print(f"Your score is {player_scores[player]}.\n")
                        print("End of turn!\n")
                        break
                else:
                    print(f"You finished this round with {player_scores[player]} points.")
                    print()
                    break

    print(f"Player #{player+1} won the game with {player_scores[player]} points!")

if __name__ == "__main__":
    main()

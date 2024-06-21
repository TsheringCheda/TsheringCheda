import random

MIN, MAX = 1, 6
class Player:
    def __init__(self, name:str ,score: int=0, turn:bool=False):
        self.name = name
        self.score = score
        self.turn = turn

    def rollDice(self):
        roll = random.randint(MIN, MAX)
        self.score += roll

run = True



p1 = Player('shit1')
p2 = Player('shit2')
p3 = Player('shit3')


player = [p1, p2, p3]

def main():
    pass


if __name__ == "__main__":
    main()


# while True: 
#     players = input("Enter the number of players (1-4): ")
#     if players.isdigit():
#         players = int(players)
#         if 2<= players <= 4:
#              break 
#         else: 
#             print("Must be between 2-4 players.")
#     else:
#         print ("Invalid, try again")

# max_score = 50
# player_scores = [0 for _ in range(players)]

# while max(player_scores) < max_score:

#     for player_tdx in range(players):
#         print("\nplayer")
#     current_score = 0

#     while True:
#         should_roll = input("woluld you like to roll (y)?")
#         if should_roll.lower() != "y":
#             break

#         value = roll()
#         if value == 1:
#             print("you rolled a 1! turn done!")
#             current_score = 0
#             break
#         else:
#             current_score += value 
#             print("you rolled a:", value)

#         print("Your score is:", current_score)

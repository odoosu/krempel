# create board
board = "---\n---\n---"
print(board)


# create players
class Players:
    # name, mark
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    # game start
    def game_turn(self):
        game_active = True
        while True:
            choice = input("place ur mark")
            try:
                choice = int(choice)
            except ValueError:
                print("must be number between 1 and 9")
            else:
                if choice >= 1 and choice >9:
                    TicTacToe.place_mark(current_player.mark)
                    return choice
                else:
                    print("must be number between 1 and 9")

    # switch turn
        def switch_turns(self, player1, player2, current_player):
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1


player1 = Players(input("First player's name:"), "X")
player2 = Players(input("Second player's name:"), "O")
print(player1.name, "is playing against", player2)

current_player = player1
game_active = True

# create game
class TicTacToe:
    def __init__(self, target, choice):
        self.target = target
        self.choice = choice

    choice = int(input("choose a spot:\n"))

    while game_active:
        print("current player is", current_player)
        choice = Players.game_turn()
        if choice:
            board[choice] = current_player.mark
            print(board)
            Players.switch_turns()

# choose spot
    def game_turn(self):
        game_active
        while True:
            Players.choice = input("place ur mark:")
            try:
                Players.choice = int(Players.choice)
            except ValueError:
                print("must be a number between 1 and 9.")
            else:
                if Players.choice >= 1 and Players.choice <= 9:
                    return Players.choice
                else:
                    print("must be a number between 1 and 9")
# set mark
    def set_mark(self, target, mark):
        self.target = target
        self.mark = mark

        target = Players.choice - 1
        if current_player is True:
            while target != "-":
                print("spot already taken, choose a different one")
            board[target] = mark
            print(board)
            self.switch_turns
# win
# lose
# tie

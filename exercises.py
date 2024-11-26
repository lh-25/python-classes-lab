class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("The game ended in a tie!")
        elif self.winner:
            print(f"Player {self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move not in self.board:
                print("Invalid move. Please choose a valid position.")
            elif self.board[move]:
                print("That space is already taken. Choose another spot.")
            else:
                return move

    def check_for_winner(self):
        win_conditions = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'], 
            ['a1', 'a2', 'a3'], 
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'], 
            ['c1', 'b2', 'a3'], 
        ]
        for condition in win_conditions:
            if all(self.board[cell] == self.turn for cell in condition):
                self.winner = self.turn
                return True
        return False

    def check_for_tie(self):
        if all(self.board[key] is not None for key in self.board) and not self.winner:
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn
            if self.check_for_winner():
                break
            if self.check_for_tie():
                break
            self.switch_turn()
        self.render()

game_instance = Game()
game_instance.play_game()

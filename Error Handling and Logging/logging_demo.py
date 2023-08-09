import logging
print(logging.__file__)

def logging_demo():

    print(logging.__file__)
    # Configure logging
    logging.basicConfig(filename='demo.log',
                       level=logging.DEBUG,
                       format='%(asctime)s - %(levelname)s - %(message)s')

    # Log messages of different levels
    logging.debug('This is a debug message.')
    logging.info('This is an info message.')
    logging.warning('This is a warning message.')
    logging.error('This is an error message.')
    logging.critical('This is a critical message.')

    try:
        result = 10 / 0
    except ZeroDivisionError:
        # Log an exception with traceback
        logging.exception('An error occurred:')

    # Logging variable data
    name = 'Alice'
    age = 30
    logging.info(f'{name} is {age} years old.')

    # Closing remarks
    logging.info('Logging demonstration completed.')



class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False

        # Setup logging
        logging.basicConfig(filename='tic_tac_toe.log',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def print_board(self):
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('-' * 9)

    def make_move(self, position):
        if not self.game_over and self.board[position] == ' ':
            self.board[position] = self.current_player
            logging.info(f'{self.current_player} placed a {self.current_player} at position {position}')
            self.check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            logging.warning('Invalid move or game already over.')

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                logging.info(f'{self.current_player} wins!')
                self.game_over = True

    def play(self):
        logging.info('Starting a new game of Tic-Tac-Toe')
        while not self.game_over:
            self.print_board()
            try:
                position = int(input(f'{self.current_player}, enter position (0-8): '))
                self.make_move(position)
            except (ValueError, IndexError):
                logging.error('Invalid input.')
        self.print_board()
        logging.info('Game over.')

if __name__ == "__main__":
    # logging_demo()
    game = TicTacToe()
    game.play()



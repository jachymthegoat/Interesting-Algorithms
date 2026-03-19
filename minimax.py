import random
import numpy as np
import utils
from utils import Player


class MinimaxPlayer(Player):
    def __init__(self):
        super().__init__()

    def next_move(self, board: np.ndarray):
        print(self.MARKER)          # +1 hodnej, -1 zlej
        print(utils.WIN_STATE_LEN)  # délka řady pro výhru
        print(board.shape)  # rozměry hracího pole
        print(board)
        print(board[0][0]) 
        print(board[0, 0]) 
        print(board[:, 0])
        print(board[1:, :-1])

        game_end, winner = utils.evaluate_board_state(board)
        if game_end:
            if winner is None:
                print("DRAW")
            if winner == self.MARKER:
                print("I won")
            if winner == 1:
                print("+1 won")
            if winner == -1:
                print("-1 won")
        print("still playing")

        best_score = float("-inf") if self.MARKER == 1 else float("inf")
        best_move = None

        for r in range(board.shape[0]):
            for c in range(board.shape[1]):
                if board[r][c] == 0:
                    # označim -> zjistim, jestli je to nejlepší -> odznačim
                    board[r][c] = self.MARKER
                    score = self.minimax(board, self.MARKER == -1)
                    board[r][c] = 0
                    # pokud jsem maximizer, tak chci nejlepší
                    if self.MARKER == 1:
                        if score > best_score:
                            best_score = score
                            best_move = (r, c)
                    # pokud jsem minimizer, tak chci nejhorší
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = (r, c)

        return best_move

    def minimax(self, board: np.ndarray, maximizing_player):
        alpha = float("-inf")
        beta = float("inf")
        
        game_end, winner = utils.evaluate_board_state(board)
        if game_end is True:
            if winner is None:
                return 0
            return winner
        
        if maximizing_player:
            best_eval = float("-inf")
            for r in range(board.shape[0]):
                for c in range(board.shape[1]):
                    if board[r, c] == 0:
                        board[r, c] = 1
                        # a co zlej
                        best_eval = max(best_eval, self.minimax(board, False))
                        board[r, c] = 0
                        alpha = max(alpha, best_eval)
                        if beta <= alpha:
                            break
            return best_eval
        else:
            min_eval = float("inf")
            for r in range(board.shape[0]):
                for c in range(board.shape[1]):
                    if board[r, c] == 0:
                        board[r, c] = -1
                        # a co hodnej
                        min_eval = min(min_eval,self.minimax(board, True))
                        board[r, c] = 0
                        beta = min(beta, min_eval)
                        if beta <= alpha:
                            break
            return min_eval
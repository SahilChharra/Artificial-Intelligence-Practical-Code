from copy import deepcopy

class TicTacToeNode:
      def __init__(self, board = None, player = "O"):
          if board is None:
              board = [[" " for _ in range(3)] for _ in range(3)]
          self.board = board
          self.player = player

      def children(self):
          if self.winner() is not None:
              return

          for row_num in range(3):
              for col_num in range(3):
                  if self.board[row_num][col_num] == " ":
                      next_board = deepcopy(self.board)
                      next_board[row_num][col_num] = self.player
                      next_player = "O" if self.player == "X" else "X"
                      yield TicTacToeNode(board = next_board, player = next_player)

      def winner(self):
          # Check for horizontal winners
          for row_num in range(3):
              if self.board[row_num][0] == self.board[row_num][1] == self.board[row_num][2] != " ":
                  return self.board[row_num][0]

          # Check for vertical winners
          for col_num in range(3):
              if self.board[0][col_num] == self.board[1][col_num] == self.board[2][col_num] != " ":
                  return self.board[0][col_num]

          # Check for diagonal winners
          if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
              return self.board[1][1]

          if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
              return self.board[1][1]

          # Check for draw
          if " " not in "".join(["".join(row) for row in self.board]):
              return 'D'

          return None

      def __str__(self):
          row_strings = [" | ".join(row) for row in self.board]
          return ("\n" + '-'*9 + "\n").join(row_strings)
      
n = TicTacToeNode()

def minimax_value(node):
      if node.winner() is not None:
          return 1 if node.winner() == 'O' else 0 if node.winner() == 'D' else -1

      child_values = [minimax_value(child) for child in node.children()]

      assert(len(child_values) > 0)

      if node.player == 'O':
          return max(child_values)
      else:
          return min(child_values)

n = next(next(TicTacToeNode().children()).children())
print(f'Minimax value for non-empty board is: {minimax_value(n)}')
print(n)     
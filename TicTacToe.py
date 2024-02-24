class TicTacToe:
  def __init__(self):
      self.board = [[' ' for _ in range(3)] for _ in range(3)]
      self.current_player = "X"

  def is_valid_move(self, row, col):
      return self.board[row][col] == ' '

  def make_move(self, row, col):
      if self.is_valid_move(row, col):
          self.board[row][col] = self.current_player
          self.switch_player()

  def switch_player(self):
      if self.current_player == "X":
          self.current_player = "O"
      else:
          self.current_player = "X"

  def check_winner(self):
      for row in range(3):
          if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
              return self.board[row][0]
      for col in range(3):
          if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
              return self.board[0][col]
      if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
          return self.board[0][0]
      if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
          return self.board[0][2]
      if not any((' ' in row for row in self.board)):
          return "T"  
      return None

def print_board(board):
  for row in board:
      print("|".join(row))
      print("-" * 5)

def main():
  game = TicTacToe()
  while True:
      print_board(game.board)
      row = int(input(f"Player {game.current_player}, enter row (0-2): "))
      col = int(input(f"Player {game.current_player}, enter col (0-2): "))
      if 0 <= row < 3 and 0 <= col < 3:
          game.make_move(row, col)
          winner = game.check_winner()
          if winner:
              print(f"Player {winner} wins!")
              break
      else:
          print("Invalid input, try again.")

if __name__ == "__main__":
  main()
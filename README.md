# Tic-Tac-Toe


## Problem description:

* The game board is an empty 3x3 grid.
* There is one human player and one computer player.
* The human player selects an unoccupied position by selecting an integer from 1-9.
* The computer player selects a random unoccupied position.
* If any player selects an occupied position then they forfeit their turn.
* Each player's marker is placed on the board in their selected position.
* After each player's turn the board is checked for game over conditions.
* If any one player's markers fill a horizontal, vertical, diagonal or antidiagonal, then that player wins the game.
* If the board is full and no player has won then a tiebreak is declared
* After the game is over, the player is prompted to play again. The user can choose to play again or quit.


## Design

* Tictactoe
  - [ ] Has two players (1 cpu, 1 human)
  - [ ] `play()` method
    - [ ] Displays game board
    - [ ] For each of the two players
      - [ ] Gets player selection
      - [ ] Attempts to place marker on selected position
      - [ ] If the board raises an exception then the turn is forfeited
      - [ ] Displays the update game board
      - [ ] Checks the board to see if the game is over
        - [ ] If one player has 3 in a row (winner)
          - [ ] Horizontal
          - [ ] Vertical
          - [ ] Diagonal
          - [ ] Antidiagonal
        - [ ] No free positions + no winner -> tiebreak
    - [ ] If the game isn't over start over again
    - [ ] Prompt the player to play again (y/N)
    ```
    def play(self):
        self.ui.welcome()
        while True:
            while True:
                for turn in 'player', 'cpu':
                    if turn == 'player':
                        selection = self.ui.prompt_player_selection()
                    else:
                        selection = randint(1, 9)
                        self.ui.display_cpu_selection(selection)
                    try:
                        self.board.place_marker(selection)
                    except (ValueError, IndexError) as err:
                        self.ui.display_error_message(err.msg)
                    self.ui.display_board(self.board)
                    if self.game_is_over():
                        break
            self.ui.display_result(self.result)
            if not self.ui.prompt_play_again()
                break
    ```

* UserInterface
  - [ ] Displays messages to user
    - [ ] Welcome message
    - [ ] The board status and position numbers  # XXX
    - [ ] Prompts for input
    - [ ] Displays cpu selection
  - [ ] Reads input from user


* Player
  - [ ] Is either a cpu or a human
  - [ ] Has a marker ('X' or 'O')
  - [ ] Can make a selection
    - [ ] From stdin (human)
    - [ ] A pseudo-random number {cpu)

* Board
  - [ ] A 3x3 grid -> 9 total positions
    ```
    board.size = 3
    ```
  - [ ] Can place a marker (single char) in an empty position
    - [ ] Raises an exception if position isn't empty
    ```
    try:
        board.place_marker(position)
    except (ValueError, IndexError) as err:
        # position not an int -> ValueError
        # position out of range -> IndexError
        print(err.msg)
    ```

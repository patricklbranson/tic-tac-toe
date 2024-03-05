#  Copyright 2024 Patrick L. Branson
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import tkinter as tk
from tkinter import messagebox as mb
from tkinter.font import Font


class TicTacToe:
    """
    The Classic tic-tac-toe game
    """

    __root: tk.Tk
    """
    The root (main) screen
    """

    __buttons = list[tk.Button]
    """
    The one-dimensional array (list) of buttons
    """

    __board: list[str]
    """
    The storage array of the moves and empty spaces
    """

    __current_player: str
    """
    The current player which is either X or O
    """

    def __init__(self):
        """
        Initializes the Tic-Tac-Toe board
        """
        self.__root = tk.Tk()
        self.__init_gui()
        self.__run_gui()

    def __init_gui(self):
        """
        Initializes the Graphical User Interface (GUI)

        :return: None -> "void" function
        """
        self.__root.title("Tic-tac-Toe")
        self.__current_player = "X"
        self.__board = [" " for _ in range(9)]

        # Creates the buttons
        self.__buttons = [
            tk.Button(
                master=self.__root,
                text=" ",
                width=5,
                height=2,
                font=Font(family="Helvetica", size=24),
                command=lambda index=i: self.__make_move(index)
            ) for i in range(9)
        ]

        # Places the buttons on the grid
        for i, button in enumerate(self.__buttons):
            row, column = divmod(i, 3)
            button.grid(row=row, column=column)

    def __run_gui(self):
        """
        Runs the Graphical User Interface (GUI) i.e. self.__root.mainloop()

        :return: None -> "void" function
        """
        self.__root.mainloop()

    def __make_move(self, index: int):
        """
        Generates the user's input to a valid move, determines if there is a winner or a draw, and/or switches over to
        the second player

        :param index: the index within the board-list
        :return: None -> "Void" function
        """
        if self.__board[index] == " ":
            self.__board[index] = self.__current_player
            self.__buttons[index].config(text=self.__current_player)

            # Checks for winners
            if self.__check_for_winner():
                mb.showinfo(title="Winner", message=f"Player {self.__current_player} Wins!")
                self.__reset_game()

            # Checks for draws
            elif " " not in self.__board:
                mb.showinfo(title="Draw", message="The Game Is A Draw!")
                self.__reset_game()

            # Continues the game and switches player
            else:
                self.__current_player = "O" if self.__current_player == "X" else "X"

    def __check_for_winner(self) -> bool:
        """
        Checks for winning conditions

        :return: True if there are winning conditions; otherwise false
        """
        for i in range(3):
            # Checks to see if the player(s) has/have a row winning condition
            if self.__board[i * 3] == self.__board[(i * 3) + 1] == self.__board[(i * 3) + 2] != " ":
                return True
            # Checks to see if the player(s) has/have a row winning condition
            if self.__board[i] == self.__board[i + 3] == self.__board[i + 6] != " ":
                return True

        # Check to see if a player(s) has/have a diagonal winning condition
        if self.__board[0] == self.__board[4] == self.__board[8] != " ":
            return True  # Left side diagonal
        elif self.__board[2] == self.__board[4] == self.__board[6] != " ":
            return True  # Right side diagonal
        else:
            return False

    def __reset_game(self) -> None:
        """
        Resets the variables to restart the game

        :return: None - "void" function
        """
        # Resets the variables
        self.__current_player = "X"
        self.__board = [" " for _ in range(9)]
        for button in self.__buttons:
            button.config(text=" ")


# Allows the program to run from this specific file
if __name__ == "__main__":
    TicTacToe()

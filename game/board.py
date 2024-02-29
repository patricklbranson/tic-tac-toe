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

import tkinter


class Board(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("Python Tic-Tac-Toe Game")

        self.__cells = {}
        self.__init_board_display()
        self.__init_board_grid()

    def __init_board_display(self):
        pass

    def __init_board_grid(self):
        pass
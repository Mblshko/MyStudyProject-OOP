from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple([tuple([Cell() for _ in range(3)]) for _ in range(3)])
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    def init(self):
        for row in self.pole:
            for cell in row:
                cell.value = TicTacToe.FREE_CELL
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def show(self):
        for row in self.pole:
            for cell in row:
                print('#' if cell.value == 0 else 'X' if cell.value == 1 else '0', end=' ')
            print()
        print('_______')

    def human_go(self):
        i = int(input('Напишите номер строчки от 1 до 3: '))
        j = int(input('Напишите номер столбика от 1 до 3: '))
        if self.pole[i-1][j-1].value == TicTacToe.FREE_CELL:
            self.pole[i-1][j-1].value = TicTacToe.HUMAN_X
        else:
            self.human_go()

    def computer_go(self):
        i = randint(0, 2)
        j = randint(0, 2)
        if self.pole[i][j].value == TicTacToe.FREE_CELL:
            self.pole[i][j].value = TicTacToe.COMPUTER_O
        else:
            self.computer_go()

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value):
        self.__is_human_win = value

    def human_win(self):
        win_ij = 0
        win_ji = 0
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == TicTacToe.HUMAN_X:
                    win_ij += 1
                if self.pole[j][i].value == TicTacToe.HUMAN_X:
                    win_ji += 1
            if win_ij == 3 or win_ji == 3:
                self.is_human_win = True
                return
            else:
                win_ij = 0
                win_ji = 0

        win_ii = 0
        win_jj = 0
        for i in range(3):
            if self.pole[i][i].value == TicTacToe.HUMAN_X:
                win_ii += 1
            if self.pole[i][-1 - i].value == TicTacToe.HUMAN_X:
                win_jj += 1
        if win_ii == 3 or win_jj == 3:
            self.is_human_win = True
            return
        self.is_human_win = False
        return

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value):
        self.__is_computer_win = value

    def computer_win(self):
        win_ij = 0
        win_ji = 0
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == TicTacToe.COMPUTER_O:
                    win_ij += 1
                if self.pole[j][i].value == TicTacToe.COMPUTER_O:
                    win_ji += 1
            if win_ij == 3 or win_ji == 3:
                self.is_computer_win = True
                return
            else:
                win_ij = 0
                win_ji = 0
        win_ii = 0
        win_jj = 0
        for i in range(3):
            if self.pole[i][i].value == TicTacToe.COMPUTER_O:
                win_ii += 1
            if self.pole[i][-1 - i].value == TicTacToe.COMPUTER_O:
                win_jj += 1
        if win_ii == 3 or win_jj == 3:
            self.is_computer_win = True
            return
        self.is_computer_win = False
        return

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value):
        self.__is_draw = value

    def __is_draw(self):
        if self.is_computer_win == False and self.is_human_win == False:
            self.is_draw = True
            return
        else:
            self.is_draw = False
            return

    def __check_index(self, index):
        i, j = index
        if type(i) != int or type(j) != int or not 0 <= i <= 2 or not 0 <= j <= 2:
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        i, j = key
        self.pole[i][j].value = value
        self.__bool__()

    def __bool__(self):
        x = 0
        for row in self.pole:
            for cell in row:
                if self.human_win() or self.computer_win():
                    break
                if cell.value == 0:
                    x += 1
                    break
        return x > 0


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
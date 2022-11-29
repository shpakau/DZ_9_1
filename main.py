# Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие
# методы:
# new_game() – для создания новой игры;
# get_field() – для получения поля (список списков);
# check_field() – для проверки, есть ли победитель, который возвращает X, если победил первый игрок, 0,
# если второй, D, если ничья и None, если можно продолжать игру;
# make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col,
# если это возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе
# крестиков,
# «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть», если победитель после
# данного хода неопределён.
# Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке
# уже стоит крестик или нолик, и «Игра уже завершена», если в текущей игре уже выявлен победитель или
# закончились ячейки для ходов.
# При создании объекта класса должна создаваться новая игра.
# Аргументы row и col метода make_move могут принимать значения от 1 до 3.

# Пример:
# board = TicTacToeBoard()
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(board.make_move(3, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")

class TicTacToeBoard:
    winner = 0
    player = 2
    per = ''
    r21 = '-'
    r22 = '-'
    r23 = '-'
    r31 = '-'
    r32 = '-'
    r33 = '-'
    r41 = '-'
    r42 = '-'
    r43 = '-'
    o = ''
    x = ''

    def check(self):
        if self.r21 == 'X' and self.r31 == 'X' and self.r41 == 'X' \
                or self.r22 == 'X' and self.r32 == 'X' and self.r42 == 'X' \
                or self.r23 == 'X' and self.r33 == 'X' and self.r43 == 'X' \
                or self.r21 == 'X' and self.r22 == 'X' and self.r23 == 'X' \
                or self.r31 == 'X' and self.r32 == 'X' and self.r33 == 'X' \
                or self.r41 == 'X' and self.r42 == 'X' and self.r43 == 'X' \
                or self.r21 == 'X' and self.r32 == 'X' and self.r43 == 'X' \
                or self.r23 == 'X' and self.r32 == 'X' and self.r41 == 'X':
            return 'Победитель игрок X'
        elif self.r21 == '0' and self.r31 == '0' and self.r41 == '0' \
                or self.r22 == '0' and self.r32 == '0' and self.r42 == '0' \
                or self.r23 == '0' and self.r33 == '0' and self.r43 == '0' \
                or self.r21 == '0' and self.r22 == '0' and self.r23 == '0' \
                or self.r31 == '0' and self.r32 == '0' and self.r33 == '0' \
                or self.r41 == '0' and self.r42 == '0' and self.r43 == '0' \
                or self.r21 == '0' and self.r32 == '0' and self.r43 == '0' \
                or self.r23 == '0' and self.r32 == '0' and self.r41 == '0':
            return 'Победитель игрок 0'
        elif self.r21 != '-' and self.r22 != '-' and self.r23 != '-' \
                and self.r31 != '-' and self.r32 != '-' and self.r33 != '-' \
                and self.r41 != '-' and self.r42 != '-' and self.r43 != '-':
            return 'Ничья'
        else:
            return 'Игра продолжаеться'

    def row1(self, r1='-', r2='-', r3='-'):
        if self.r21 == '-' and r1 is not None:
            if r1 != '-':
                self.r21 = r1
                return self.check()
            else:
                self.r21 = '-'

        if self.r22 == '-':
            if r2 != '-':
                self.r22 = r2
                return self.check()
            else:
                self.r22 = '-'

        if self.r23 == '-':
            if r3 != '-':
                self.r23 = r3
                return self.check()
            else:
                self.r23 = '-'
        return [self.r21, self.r22, self.r23]

    def row2(self, r1='-', r2='-', r3='-'):
        if self.r31 == '-' and r1 is not None:
            if r1 != '-':
                self.r31 = r1
                return self.check()
            else:
                self.r31 = '-'

        if self.r32 == '-':
            if r2 != '-':
                self.r32 = r2
                return self.check()
            else:
                self.r32 = '-'

        if self.r33 == '-':
            if r3 != '-':
                self.r33 = r3
                return self.check()
            else:
                self.r33 = '-'

        return [self.r31, self.r32, self.r33]

    def row3(self, r1='-', r2='-', r3='-'):
        if self.r41 == '-':
            if r1 != '-' and r1 is not None:
                self.r41 = r1
                return self.check()
            else:
                self.r41 = '-'

        if self.r42 == '-':
            if r2 != '-' and r2 is not None:
                self.r42 = r2
                return self.check()
            else:
                self.r42 = '-'

        if self.r43 == '-':
            if r3 != '-':
                self.r43 = r3
                return self.check()
            else:
                self.r43 = '-'
        return [self.r41, self.r42, self.r43]

    def new_game(self):
        self.winner = 0
        self.player = 2
        self.per = '-'
        self.r21 = '-'
        self.r22 = '-'
        self.r23 = '-'
        self.r31 = '-'
        self.r32 = '-'
        self.r33 = '-'
        self.r41 = '-'
        self.r42 = '-'
        self.r43 = '-'
        self.o = ''
        self.x = ''

    def get_field(self):
        return self.row1(), self.row2(), self.row3()

    def check_winner(self, s):
        if s == 'Победил игрок X':
            self.winner += 1
            self.x = 1
            return 'Победил игрок X'
        elif s == 'Победил игрок 0':
            self.winner += 1
            self.o = 1
            return 'Победил игрок 0'
        elif s == "Ничья":
            self.winner -= 1
            return 'Ничья'
        else:
            return 'Продолжаем играть'

    def check_field(self):
        if self.x == 1:
            return 'X'
        elif self.o == 1:
            return '0'
        elif self.winner == -1:
            return 'D'
        else:
            return None

    def make_move(self, row, col):
        if self.winner == 0:
            if self.player == 2:  # ----------------------- выбор игрока:
                self.per = 'X'
                self.player += 1
            else:
                self.per = '0'
                self.player -= 1
            # --------------------------------------------- игрок делает свой ход
            if row == 1:
                if col == 1 and self.r21 == '-':
                    s = self.row1(self.per)
                    return self.check_winner(s)
                elif col == 2 and self.r22 == '-':
                    s = self.row1(None, self.per)
                    return self.check_winner(s)
                elif col == 3 and self.r23 == '-':
                    s = self.row1(None, None, self.per)
                    return self.check_winner(s)
                else:
                    if self.player == 3:
                        self.player -= 1
                    else:
                        self.player += 1
                    return 'Клетка ' + str(row) + ', ' + str(col) + ' занята'
            elif row == 2:
                if col == 1 and self.r31 == '-':
                    s = self.row2(self.per)
                    return self.check_winner(s)
                elif col == 2 and self.r32 == '-':
                    s = self.row2(None, self.per)
                    return self.check_winner(s)
                elif col == 3 and self.r33 == '-':
                    s = self.row2(None, None, self.per)
                    return self.check_winner(s)
                else:
                    if self.player == 3:
                        self.player -= 1
                    else:
                        self.player += 1
                    return 'Клетка ' + str(row) + ', ' + str(col) + ' занята'
            elif row == 3:
                if col == 1 and self.r41 == '-':
                    s = self.row3(self.per)
                    return self.check_winner(s)
                elif col == 2 and self.r42 == '-':
                    s = self.row3(None, self.per)
                    return self.check_winner(s)
                elif col == 3 and self.r43 == '-':
                    s = self.row3(None, None, self.per)
                    return self.check_winner(s)
                else:
                    if self.player == 3:
                        self.player -= 1
                    else:
                        self.player += 1
                    return 'Клетка ' + str(row) + ', ' + str(col) + ' занята'
        else:
            return 'Игра завершена'


board = TicTacToeBoard()
print(*board.get_field(), sep='\n')
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
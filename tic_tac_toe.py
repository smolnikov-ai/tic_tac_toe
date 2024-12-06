# smolnikov-ai 06-12-2024 smolnikov-ai@mail.ru 920-066-20-90

import time
import random

"""
Реализует в консоли игру крестики-нолики.
Возможен режим для одного игрока - противник компьютер.
Возможен режим для двух игроков.
"""

# Глобальная переменная - режим игры (один игрок, два игрока)
mode = None
# Глобальные переменные - имена игроков
name_gamer_x = 'Крестик'
name_gamer_o = 'Нолик'
# Глобальная переменная - словарь с данными для клеток игрового поля
fld = {'a0': ' ', 'b0': ' ', 'c0': ' ', 'a1': ' ', 'b1': ' ', 'c1': ' ', 'a2': ' ', 'b2': ' ', 'c2': ' '}

def get_data():
    """
    Запуск игры. Вывод правил игры. Выбор режима (PvE, PvP). Получение от пользователя имен игроков.
    """
    global name_gamer_x, name_gamer_o
    print('Добро пожаловать в игру крестики-нолики.')
    time.sleep(1)
    print('Правила просты.')
    time.sleep(1)
    print('Имеется поле 3 на 3 клетки.')
    time.sleep(1)
    show_game_field()
    time.sleep(1)
    print('Игроки поочередно выбирают клетку в виде a0, b0, c2...')
    time.sleep(2)
    print('Выбранная клетка заполняется символом.')
    time.sleep(2)
    print('Побеждает тот, кто первым соберет в линию три одинаковых символа.')
    time.sleep(2)
    print('Доступно два режима игры - одиночная и для двоих.')
    time.sleep(1)
    print()
    print('Введите')
    time.sleep(1)
    print('1 - для одиночной игры в режиме PvE')
    time.sleep(1)
    print('2 - для игры вдвоем в режиме PvP')
    mode_definition()

    if mode == '1':
        # При отсутствии имени игрока (enter), устанавливается имя по умолчанию
        print()
        name_gamer_o = input('Введите имя игрока: ')
        if not name_gamer_o:
            name_gamer_o = 'Нолик'
        time.sleep(1)
        print()
        print(f'Игрок {name_gamer_o}, Ваш символ - ○')
        time.sleep(1)
        print()
        print('Computer на чистом randome, поэтому ходит первым.')
        make_move_pve()

    else:
        name_gamer_x = input('Введите имя первого игрока: ')
        # При отсутствии имени игрока (enter), устанавливается имя по умолчанию
        if not name_gamer_x:
            name_gamer_x = 'Крестик'
        time.sleep(1)
        name_gamer_o = input('Введите имя второго игрока: ')
        # При отсутствии имени игрока (enter), устанавливается имя по умолчанию
        if not name_gamer_o:
            name_gamer_o = 'Нолик'
        print(f'Игрок {name_gamer_x}, Ваш символ - ✗')
        time.sleep(1)
        print(f'Игрок {name_gamer_o}, Ваш символ - ○')
        make_move_pvp()

def mode_definition():
    """
    Запрос у пользователя режима игры.
    :return:
    str '1' или '2'
    """
    global mode
    time.sleep(1)
    print()
    mode = input('Жду вашего решения, 1 или 2: ')
    if mode != '1' and mode != '2':
        print()
        print('Попробуйте снова, PvE or PvP?')
        time.sleep(1)
        mode_definition()
    return mode

def show_game_field():
    """
    Выводит на экран игровое поле 3х3
    """

    print(f'                         a     b     c\n'
          f'                       ----- ----- -----\n'
          '                    0 |' + "  " + f'{fld['a0']}' + "  " + "|" + "  " + f'{fld['b0']}' + "  " + "|" + "  "
          + f'{fld['c0']}' + "  " + "|" + f'\n'
          f'                       ----- ----- -----\n'
          '                    1 |' + "  " + f'{fld['a1']}' + "  " + "|" + "  " + f'{fld['b1']}' + "  " + "|" + "  "
          + f'{fld['c1']}' + "  " + "|" + f'\n'
          f'                       ----- ----- -----\n'
          '                    2 |' + "  " + f'{fld['a2']}' + "  " + "|" + "  " + f'{fld['b2']}' + "  " + "|" + "  "
          + f'{fld['c2']}' + "  " + "|" + f'\n'                                                                                     
          f'                       ----- ----- -----'
          )

def make_move_pvp():
    """
    Обработка ходов в режиме PvP
    :return:
    Завершает программу в случае победы или ничьи
    """
    while True:
        time.sleep(1)
        move_gamer_x()
        # Условие победы игрока name_gamer_x
        if win_gamer_x():
            show_game_field()
            time.sleep(1)
            print(f'|||||||||||                                       |||||||||||')
            print(f'            Победил игрок {name_gamer_x}. Поздравляем!!!')
            print(f'|||||||||||                                       |||||||||||')
            return
        # Условие окончания игры по отсутствию пустых клеток. После хода name_gamer_x т.к. на девятую клетку ходит он
        if not list(filter(lambda x: x == ' ', fld.values())):
            time.sleep(1)
            show_game_field()
            time.sleep(1)
            print('Победителя выявить не удалось.')
            time.sleep(1)
            print('_____________________________ НИЧЬЯ !!! _____________________________')
            time.sleep(1)
            print('_____________________________ GAME OVER _____________________________')
            return
        time.sleep(1)
        move_gamer_o()
        # Условие победы игрока name_gamer_o
        if win_gamer_o():
            show_game_field()
            time.sleep(1)
            print(f'|||||||||||                                     |||||||||||')
            print(f'            Победил игрок {name_gamer_o}. Поздравляем!!!')
            print(f'|||||||||||                                     |||||||||||')
            return

def make_move_pve():
    """
    Обработка ходов в режиме PvE
    :return:
    Завершает программу в случае победы или ничьи
    """
    while True:
        time.sleep(1)
        move_computer()
        # Условие победы игрока computer - аналогичны игроку за '✗'
        if win_gamer_x():
            show_game_field()
            time.sleep(1)
            print(f'|||||||||||                                                |||||||||||')
            print(f'            Победил computer. И скоро захватит весь мир...')
            print(f'|||||||||||                                                |||||||||||')
            return
        # Условие окончания игры по отсутствию пустых клеток. После хода сcomputer т.к. на девятую клетку ходит он
        if not list(filter(lambda x: x == ' ', fld.values())):
            time.sleep(1)
            show_game_field()
            time.sleep(1)
            print('Победителя выявить не удалось.')
            time.sleep(1)
            print('_____________________________ НИЧЬЯ !!! _____________________________')
            time.sleep(1)
            print('_____________________________ GAME OVER _____________________________')
            return
        time.sleep(3)
        move_gamer_o()
        # Условие победы игрока name_gamer_o
        if win_gamer_o():
            show_game_field()
            time.sleep(1)
            print(f'|||||||||||                                   |||||||||||')
            print(f'            Кожанный победил. I will be back!')
            print(f'|||||||||||                                   |||||||||||')
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            print("BO-O-O-OM")
            return

def move_gamer_x():
    """
    Обрабатывает ход игрока gamer_x
    """
    global fld
    show_game_field()
    time.sleep(1)
    print()
    print(f'____________________ Игрок {name_gamer_x} Ваш ход. ____________________')
    cell = input(f'Выберите пустую клетку: ')
    # Проверка наличия клетки на поле
    # Если клетки на поле нет - выбираем другую тем же игроком
    if not cell in fld.keys():
        time.sleep(1)
        print(f'Такой клетки нет.')
        time.sleep(1)
        # Предлагаем на выбор перечень пустых клеток
        print('Выберите одну из клеток')
        print(*ident_empty_cell(), sep=', ')
        time.sleep(1)
        move_gamer_x()
    else:
        # Если клетка на поле есть и она пустая, заполняем
        if fld[cell] == ' ':
            print()
            fld[cell] = '✗'
        # Если клетка занята - выбираем другую тем же игроком
        else:
            time.sleep(1)
            print()
            print('Клетка занята.')
            time.sleep(1)
            print('Выберите одну из клеток')
            print(*ident_empty_cell(), sep=', ')
            print()
            time.sleep(1)
            move_gamer_x()

def move_gamer_o():
    """
    Обрабатывает ход игрока gamer_o
    """
    global fld
    show_game_field()
    time.sleep(1)
    print()
    print(f'____________________ Игрок {name_gamer_o} Ваш ход. ____________________')
    cell = input(f'Выберите пустую клетку: ')
    # Проверка наличия клетки на поле
    # Если клетки на поле нет - выбираем другую тем же игроком
    if not cell in fld.keys():
        time.sleep(1)
        print(f'Такой клетки нет.')
        time.sleep(1)
        # Предлагаем на выбор перечень пустых клеток
        print('Выберите одну из клеток')
        print(*ident_empty_cell(), sep=', ')
        time.sleep(1)
        move_gamer_o()
    else:
        # Если клетка на поле есть и она пустая, заполняем
        if fld[cell] == ' ':
            print()
            fld[cell] = '○'
        # Если клетка занята - выбираем другую тем же игроком
        else:
            time.sleep(1)
            print()
            print('Клетка занята.')
            time.sleep(1)
            print('Выберите одну из клеток')
            print(*ident_empty_cell(), sep=', ')
            print()
            time.sleep(1)
            move_gamer_o()

def move_computer():
    """
    Обрабатывает ход Computer

    Computer ходит первым и ставит '✗'
    """
    global fld
    show_game_field()
    time.sleep(1)
    print()
    print(f'_______________________ Ходит Computer _______________________')
    print()
    cell = random.choice(ident_empty_cell())
    fld[cell] = '✗'

def win_gamer_x():
    """
    Определяет победу игрока name_gamer_x (наличие трех '✗' в ряду) и computer
    :return:
    True - в случае победы, иначе - False
    """
    if fld['a0'] == fld['b0'] == fld['c0'] == '✗' or fld['a1'] == fld['b1'] == fld['c1'] == '✗' or\
            fld['a2'] == fld['b2'] == fld['c2'] == '✗' or fld['a0'] == fld['a1'] == fld['a2'] == '✗' or\
            fld['b0'] == fld['b1'] == fld['b2'] == '✗' or fld['c0'] == fld['c1'] == fld['c2'] == '✗' or\
            fld['a0'] == fld['b1'] == fld['c2'] == '✗' or fld['a2'] == fld['b1'] == fld['c0'] == '✗':
        return True
    else:
        return False

def win_gamer_o():
    """
    Определяет победу игрока name_gamer_o (наличие трех '○' в ряду)
    :return:
    True - в случае победы, иначе - False
    """
    if fld['a0'] == fld['b0'] == fld['c0'] == '○' or fld['a1'] == fld['b1'] == fld['c1'] == '○' or \
            fld['a2'] == fld['b2'] == fld['c2'] == '○' or fld['a0'] == fld['a1'] == fld['a2'] == '○' or \
            fld['b0'] == fld['b1'] == fld['b2'] == '○' or fld['c0'] == fld['c1'] == fld['c2'] == '○' or \
            fld['a0'] == fld['b1'] == fld['c2'] == '○' or fld['a2'] == fld['b1'] == fld['c0'] == '○':
        return True
    else:
        return False

def ident_empty_cell():
    """
    Проверяет наличие пустых клеток на поле
    :return:
    Возвращает list с пустыми клетками
    """
    _ = []
    for k, v in fld.items():
        if v == ' ':
            _.append(k)
    return _

get_data()
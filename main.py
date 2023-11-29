import numpy as np
import random
import sys
import os
import time




def field_display(field):
    for i in range(4):
        print(field[4 * i], field[4 * i + 1], field[4 * i + 2], field[4 * i + 3])
    print()

def find_null(field):
    indexes_of_null_el = []
    for i in range(16):
        if field[i] == 0:
            indexes_of_null_el.append(i)
    return indexes_of_null_el


def add_two(field):
    indexes_of_null_el = find_null(field)
    rand = random.choice(indexes_of_null_el)
    field[rand] = 2



def move_up(field):
    for i in range(11, -1, -1):
        if field[i] == 0:
            field[i] = field[i + 4]
            field[i + 4] = 0
        elif field[i] == field[i + 4]:
            field[i] *= 2
            field[i + 4] = 0


def move_down(field):
    for i in range(3, 16):
        if field[i] == 0:
            field[i] = field[i - 4]
            field[i - 4] = 0
        elif field[i] == field[i - 4]:
            field[i] *= 2
            field[i - 4] = 0


def move_right(field):
    for i in range(0, 16):
        if i % 4 != 0:
            if field[i] == 0:
                field[i] = field[i - 1]
                field[i - 1] = 0
            elif field[i] == field[i - 1]:
                field[i] *= 2
                field[i - 1] = 0


def move_left(field):
    for i in range(15, -1, -1):
        if (i + 1) % 4 != 0:
            if field[i] == 0:
                field[i] = field[i + 1]
                field[i + 1] = 0
            elif field[i] == field[i + 1]:
                field[i] *= 2
                field[i + 1] = 0


def is_win(field):
    for item in field:
        if item == 2048:
            return True
    return False

if __name__ == '__main__':
    field = np.zeros(16, dtype=int)
    add_two(field)
    add_two(field)
    while 1:
        print("Press to move - 'WASD', Press Q to quit")
        field_display(field)
        old_field = np.copy(field)
        move = input()
        if move == 'w':
            move_up(field)
            move_up(field)
        elif move == 'a':
            move_left(field)
            move_left(field)
        elif move == 's':
            move_down(field)
            move_down(field)
        elif move == 'd':
            move_right(field)
            move_right(field)
        elif move == 'q':
            sys.exit()
        if not np.array_equal(old_field, field):
            add_two(field)
        if is_win(field):
            print('CONGRATULATIONS, YOU WIN!')
            sys.exit()
        time.sleep(0.5)
        os.system('cls')

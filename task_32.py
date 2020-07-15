#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    def main():
        l = tunnel_length()
        print('длина туннеля =', l)
        t = tunnel_work(l)
        print('в туннеле закрашено клеток', t)
        count = corridor_count(l)
        print('количество корридоров =', count)
        r = 0
        v = 0
        for x in range(l):
            if wall_is_above() == False:
                move_up()
                r += 1
                v = corridor_work()
                print('в коридоре', r, 'ранее закрашенных клеток', v)
                mov(r, v)
            move_right()

        # for i in range(r):
        #     for j in range(v):
        #         print(mov(i, j))

    def corridor_work():
        filled_cells = 0
        # print('Вызов функции corridor_work')
        while wall_is_above() == False:
            if cell_is_filled() == True:
                filled_cells += 1
            else:
                fill_cell()
            if wall_is_above() == False:
                move_up()
        if cell_is_filled() == True:
            filled_cells += 1
        else:
            fill_cell()
        while wall_is_beneath() == False:
            move_down()
        # move_right()
        return filled_cells

    def corridor_length():
        y = 0
        while wall_is_above() == False:
            move_up()
            y += 1
        move_down(y)
        return y
    def corridor_count(l):
        count = 0
        for x in range(l):
            if wall_is_above() == False:
                count += 1
            move_right()
        move_left(l)
        return count

    def tunnel_work(l):
        filled_cells = 0
        for x in range(l):
            if wall_is_above() == True:
                fill_cell()
            move_right()
        for x in range(l):
            if cell_is_filled() == True:
                filled_cells += 1
            move_left()
        return filled_cells

    def final_position():
        pass
    def tunnel_length():
        x = 0
        while wall_is_beneath() == True:
            move_right()
            x += 1
        move_left(x)
        return x





    main()


if __name__ == '__main__':
    run_tasks()

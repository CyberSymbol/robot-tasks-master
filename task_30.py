#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    def paint_up_triangle():
        for i in range(3):
            move_right()
            fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()
        move_left(2)

    def paint_left_triangle():
        for i in range(3):
            move_down()
            fill_cell()
        move_up()
        move_right()
        fill_cell()
        move_left()
        move_up(2)

    def paint_right_triangle():
        for i in range(3):
            move_down()
            fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right()
        move_up(2)

    def paint_down_triangle():
        for i in range(3):
            move_right()
            fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_down()
        move_left(2)

    def square_side_length():
        x = 1
        while wall_is_on_the_right() == False:
            x += 1
            move_right()
        else:
            move_left(x - 1)
            return x

    l = square_side_length()
    for i in range(l // 3):
        paint_up_triangle()
        paint_left_triangle()
        move_right(l-1)
        paint_right_triangle()
        move_left(l-1)
        move_down(l-1)
        paint_down_triangle()


if __name__ == '__main__':
    run_tasks()

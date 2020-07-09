#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    def paint_upper_triangle():
        for i in range(2):
            move_right()
            fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()
        move_left()

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
        paint_upper_triangle()

if __name__ == '__main__':
    run_tasks()

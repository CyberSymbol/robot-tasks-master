#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def paint_cross():
        # Становимся в центр креста
        move_down()
        move_right()
        # Закрашиваем крест
        fill_cell()
        move_right()
        fill_cell()
        move_left(2)
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_down(2)
        fill_cell()
        move_up()
        # Возвращаемся на базу
        move_up()
        move_left()
    # Конец функции
    def paint_row():
        for i in range(9):
            paint_cross()
            move_right(4)
        paint_cross()
        move_left(36)
    for i in range(4):
        paint_row()
        move_down(4)
    paint_row()

if __name__ == '__main__':
    run_tasks()

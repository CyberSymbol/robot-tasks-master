#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
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
    move_down()
    for i in range(4):
        paint_cross()
        move_right(4)
    paint_cross()


if __name__ == '__main__':
    run_tasks()

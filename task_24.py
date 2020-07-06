#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
# Становимся в центр креста    
    move_right(2)
    move_down(2)
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



if __name__ == '__main__':
    run_tasks()

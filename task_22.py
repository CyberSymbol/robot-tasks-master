#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while wall_is_beneath() == False:
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        fill_cell()
        while wall_is_on_the_left() == False:
            move_left()
        move_down()
    else :
        while wall_is_on_the_right() == False:
            fill_cell()
            move_right()
        fill_cell()
        while wall_is_on_the_left() == False:
            move_left()


if __name__ == '__main__':
    run_tasks()

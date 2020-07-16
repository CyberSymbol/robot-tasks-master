#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while wall_is_above() or wall_is_beneath():
        if not wall_is_above():
            move_up()
            move_down()
        if not wall_is_beneath():
            move_down()
            move_up()
        move_right()



if __name__ == '__main__':
    run_tasks()

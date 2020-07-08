#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    n = 0
    while n < 4:
        if cell_is_filled() == True:
            n += 1
            move_right()
        else:
            move_right()
    else:
        while cell_is_filled() == False:
            move_right()


if __name__ == '__main__':
    run_tasks()

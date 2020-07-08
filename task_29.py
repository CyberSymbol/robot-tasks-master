#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    n = 0
    while n < 3:
        if cell_is_filled() == True:
            n += 1
            if n == 3:
                break
            if wall_is_on_the_right() == False:
                move_right()
            else:
                break
        else:
            n = 0
            if wall_is_on_the_right() == False:
                move_right()
            else:
                break




if __name__ == '__main__':
    run_tasks()

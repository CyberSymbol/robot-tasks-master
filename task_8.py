#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while wall_is_above() == True:
        move_right()
    else:
        move_up()
        move_right()
    while wall_is_beneath() == True:
        move_right()
    else:
        move_down()
        move_right()
    while wall_is_above() == True or wall_is_beneath() == True :
        move_right()

if __name__ == '__main__':
    run_tasks()

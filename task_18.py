#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while wall_is_on_the_left() == False : 
        move_left()
    while wall_is_on_the_right() == False :
        if wall_is_above() == False :
            while wall_is_beneath() == True :
                move_up()
            else:
                break
        else :
            move_right()
    while wall_is_above() == False :
        move_up()
    while wall_is_on_the_left() == False :
        move_left()                


if __name__ == '__main__':
    run_tasks()

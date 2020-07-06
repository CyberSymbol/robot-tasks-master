#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_right() == False :
        while wall_is_on_the_right() == False :
            move_right()
        if wall_is_beneath() == False :
            while wall_is_beneath() == False :
                move_down()
        elif wall_is_above() == False :
            while wall_is_above() == False :
                move_up()
    elif wall_is_on_the_left() == False :
        while wall_is_on_the_left() == False :
            move_left()
        if wall_is_beneath() == False :
            while wall_is_beneath() == False :
                move_down()
        elif wall_is_above() == False :
            while wall_is_above() == False :
                move_up()


if __name__ == '__main__':
    run_tasks()

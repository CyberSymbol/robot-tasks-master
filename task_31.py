#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    def wall_length():
        x = 1
        while wall_is_on_the_left() == False:
            x += 1
            move_left()
        else:
            move_right(x - 1)
            return x

    def last_wall():
        flag = True
        while wall_is_on_the_left() == False:
            move_left()
        while wall_is_on_the_right() == False:
            if wall_is_beneath() == False:
                flag = False
            move_right()
        return flag

    def pass_one_wall(l):
        for distance in range(l):
            if wall_is_beneath() == False:
                while wall_is_beneath() == False:
                    move_down()
            else:
                if wall_is_on_the_left() == False:
                    move_left()
                    distance += 1

    l = wall_length()
    while last_wall() == False:
        pass_one_wall(l)
    while wall_is_on_the_left() == False:
        move_left()




if __name__ == '__main__':
    run_tasks()

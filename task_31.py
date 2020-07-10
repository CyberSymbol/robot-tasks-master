#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    def pass_one_wall():
        # while wall_is_on_the_left() == False:
        #     move_left()
        while wall_is_beneath() == True:
            if wall_is_on_the_left() == False:
                move_left()
        else:
            while wall_is_beneath() == False:
                move_down()
        while wall_is_on_the_right() == False:
            move_right()


    while wall_is_beneath() == True:
        pass_one_wall()
    # else:
    #     while wall_is_on_the_right() == False:
    #         move_right()




if __name__ == '__main__':
    run_tasks()

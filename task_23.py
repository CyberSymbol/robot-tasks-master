#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while wall_is_on_the_right() == False:  # пока справа нет стены
        move_right() # идём к концу туннеля
    while wall_is_beneath() == True:  # пока снизу есть стена
        if wall_is_above()  == False:
            while wall_is_above() == False: # пока не кончился коридор
                move_up() # идём по коридору вверх
                fill_cell()
            while wall_is_beneath() == False: # пока не вернулись в туннель    
                move_down()
        move_left() # идём к началу туннеля   
    

if __name__ == '__main__':
    run_tasks()

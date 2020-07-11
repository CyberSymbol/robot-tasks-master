#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    def square_side_length():
        x = 1
        while wall_is_on_the_left() == False:
            x += 1
            move_left()
        else:
            move_right(x - 1)
            return x

    def pass_one_wall(lim):
        distance = 0
        while distance < lim: # Пока не прошли весь путь
            if wall_is_on_the_left() == False and wall_is_beneath() == True: # Если слева нет стены, а снизу стена
                move_left() # Шаг влево
                distance += 1 # Записываем шаг
                print('distance =', distance)
            elif wall_is_beneath() == False:
                while wall_is_beneath() == False:
                    move_down()
        else:
            print ('ппц')
        while wall_is_on_the_right() == False:
            move_right()

    lim = square_side_length()
    print('lim =', lim)
    while wall_is_on_the_right() == False:
        move_right()
    while wall_is_beneath() == False:
        move_down()
    while wall_is_beneath() == True:
        pass_one_wall(lim)





if __name__ == '__main__':
    run_tasks()

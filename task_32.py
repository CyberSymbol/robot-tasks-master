#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    def main():
        l = tunnel_length()
        print(l)

    def corridor_work():
        pass
    def tunnel_work():
        pass
    def final_position():
        pass
    def tunnel_length():
        x = 0
        while wall_is_beneath() == True:
            move_right()
            x += 1
        move_left(x)
        return x





    main()


if __name__ == '__main__':
    run_tasks()

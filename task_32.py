#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    def main():
        filled_cells = 0
        while not wall_is_on_the_right():
            if not wall_is_above():
                filled_cells += corridor_work()
            else:
                if not cell_is_filled():
                    fill_cell()
                else:
                    filled_cells += 1
            move_right()
        mov('ax', filled_cells)

    def corridor_work():
        filled_cells = 0
        while not wall_is_above():
            move_up()
            if cell_is_filled():
                filled_cells += 1
            else:
                fill_cell()
        while not wall_is_beneath():
            move_down()
        return filled_cells

    main()

if __name__ == '__main__':
    run_tasks()

""" This module contains the answer to exercise 3 of Chapter 3.
"""


def print_add_sign():
    """Prints the add (+) sign on the corners.
    """
    print("+ ", end="")


def print_hyphens():
    """Prints the hyphens (-).
    """
    print("- ", end="")



def print_row_line(num_of_grids):
    """Prints one row line for the one square grid.
    """
    if num_of_grids < 2:
        print_add_sign()
        for _ in range(4):
            print_hyphens()
        print_add_sign()
    elif num_of_grids >= 2:
        for _ in range(num_of_grids):
            print_add_sign()
            for _ in range(4):
                print_hyphens()
        print_add_sign()




def print_bar(num_of_grids):
    """Prints the bar (|) sign on the cosole.
    """
    for _ in range(num_of_grids + 1):
        print("|".ljust(10), end="")



def print_col(num_of_grids):
    """Prints the required number of columns.
    """
    for _ in range(4):
        print("")
        print_bar(num_of_grids)
    print("")
    print_row_line(num_of_grids)


def draw_grid(num_of_grids=1):
    """Prints the number of required grids.

    Args:
        num_of_grids (int): Number of Square grids required on console.`
    """
    print_row_line(num_of_grids)
    for _ in range(num_of_grids):
        print_col(num_of_grids)

    

draw_grid(int(input()))




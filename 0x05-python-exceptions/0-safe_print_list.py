#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0  # Initialize a variable to count the printed elements

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:  # Handle the IndexError when trying to access an out-of-range element
        pass
    finally:
        print()  # Print a newline after the elements

    return printed

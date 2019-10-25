#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program multiplies all previously occuring integers including the one
# inputted and gives the Product


def main():

    # variable
    value_1_int = 0
    loop_adder = 0
    answer = 1
    # process
    # input
    value_1 = input("Enter a number of your choice: ")
    print("")
    try:
        value_1_int = int(value_1)
        while loop_adder < value_1_int:
            loop_adder += 1
            answer = loop_adder * answer
        print("The product is " + str(answer))
    except Exception:
        print("that is not an integer")


if __name__ == "__main__":
    main()

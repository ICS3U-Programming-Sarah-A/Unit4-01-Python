#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Sarah
# Modified on: Apr. 19, 2022
# This program asks the user to enter a number. It then displays the sum
# of the number the user entered using loops.

def main():
    # initialize the loop counter and sum
    loop_counter = 0
    loop_sum = 0

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")

    try:
        # converts user input to integer
        user_number_int = int(user_number_string)

        if user_number_int >= 0:
            # calculate the sum of all numbers from 0 to user number
            while (loop_counter <= user_number_int):
                loop_sum = loop_sum + loop_counter
                print("Tracking {0} times through loop.".format(loop_counter))
                loop_counter = loop_counter + 1

            print("")
            print("The sum of the numbers from 0 to {} is: {}.".
                  format(user_number_int, loop_sum))
        else:
            print("{} is not a positive integer".format(user_number_int))
    except Exception:
        print("{} is not a valid number.". format(user_number_string))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import random


# Helps find the average of any generic iterable
def average(iterable):
    return sum(iterable)/len(iterable)

# Main function
def main():
    # Input validation loop
    while True:
        try:
            # Getting the user input
            list_len = int(input("Please enter the length of the list: "))
            
            # Checking that list length is valid
            if not list_len > 0:
                print("List length needs to be greater than 0. Please try again!")
                continue
            
            l_bound = int(input("Please enter the lower bound for the range of integer values: "))
            u_bound = int(input("Please enter the upper bound for the range of integer values: "))

            # Checking that lower bound is truly lower than upper bound
            if l_bound >= u_bound:
                print("Lower bound must be less than upper bound. Please try again!")
                continue
            
            break
        # Checks and catches situations where user submits a number
        except ValueError:
            print("Input should be a number. Please try again!")
            continue

    # Generating the list
    rand = [random.randint(l_bound, u_bound) for i in range(list_len)]

    print("\n Sequence: " + str(rand))

    # Getting list parameters
    print("\nList length: {}".format(list_len))
    print("Largest integer: {}".format(max(rand)))
    print("Smallest integer: {}".format(min(rand)))
    print("Sum: {}".format(sum(rand)))
    print("Average: {}".format(average(rand)))

if __name__ == "__main__":
    main()

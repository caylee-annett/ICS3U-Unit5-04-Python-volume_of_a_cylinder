#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program calculates the volume of a cylinder and uses a return value

import math


def volume_calculation(radius, height):
    # This function calculates the volume

    volume = math.pi * radius ** 2 * height

    return volume


def main():
    # This function gets the radius and height

    # Input
    print("This program calculates the volume of a cylinder.")
    print("")
    radius_input_string = input("Enter the radius of the cylinder (cm): ")
    height_input_string = input("Enter the height of the cylinder (cm): ")

    # Process
    while True:
        try:
            radius_input_integer = int(radius_input_string)

            if radius_input_integer > 0:
                break
            else:
                radius_input_string = input("Must be a positive integer. "
                                            "Enter the radius (cm): ")
        except Exception:
            radius_input_string = input("{} is not a valid input. Enter the "
                                        "radius (cm): ".
                                        format(radius_input_string))
    while True:
        try:
            height_input_integer = int(height_input_string)

            if height_input_integer > 0:
                break
            else:
                height_input_string = input("Must be a positive integer. "
                                            "Enter the height (cm): ")
        except Exception:
            height_input_string = input("{} is not a valid input. Enter the "
                                        "height (cm): ".
                                        format(height_input_string))

    # Call functions
    calculated_volume = volume_calculation(radius_input_integer,
                                           height_input_integer)

    # Output
    print("")
    print("The volume of a cylinder with a radius of {0} cm and a height of "
          "{1} cm is {2} cm³.".
          format(radius_input_integer, height_input_integer,
                 calculated_volume))
    print("\nDone.")


if __name__ == "__main__":
    main()

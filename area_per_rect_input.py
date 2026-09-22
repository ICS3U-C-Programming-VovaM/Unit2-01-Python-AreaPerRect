#!/usr/bin/env python3
# Created By: Vova M
# Date: Sep 21, 2026
# This program asks the user for the length and width of a rectangle and calculates the area and perimeter
# back to the user with proper units
def main():
    # get the  length from the user and convert it to an integer
    length = int(input("Enter length of the rectangle (cm): "))

    # get the  width from the user and convert it to an integer
    width = int(input("Enter width of the rectangle (cm): "))

    # calculate the area and perimeter of the rectangle
    area = length * width
    perimeter = 2 * (length + width)

    # displays the area and perimeter to the user with proper units
    print("The area is: {}cm²".format(area))
    print("The perimeter is: {}cm".format(perimeter))


if __name__ == "__main__":
    main()

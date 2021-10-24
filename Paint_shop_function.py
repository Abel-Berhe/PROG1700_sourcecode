#Don't forget to rename this file after copying the template
#for a new program!
import math
"""
Student Name:   Abel Berhe 
Program Title:  PaintCalculator using function
Description:   Calculating the amount of gallon needed for particular surface space 
"""


def paintCalculator(length,width,height):
    square_feet_per_gallon = 150.0
    totalArea = (length * height * 2) + (width * height * 2)
    gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)
    return totalArea, gallons_of_paint


def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Welcome to the Paint Shop!")
    print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")
    length = float(input("\nEnter the length of the room, in feet: "))
    width = float(input("Enter the width of the room, in feet: "))
    height = float(input("Enter the height of the room, in feet: "))

    
    area,result= paintCalculator(length,width,height)
    print("\nThe total wall area of your room is {0} square feet.".format(area))
    print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(result))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()
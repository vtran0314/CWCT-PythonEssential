################################
# Program name: circle_area.py

#  Author: Vinh Tran
#  Course: Python Essentials
#  Date: 8/2/2023
#  Assignment: Module 4 - Area of a Circle
#  Purpose: Calculate an area of a circle
########################################


#d = sqrt(x2−x1)^2 + (y2−y1)^2)

import math


#TO-DO: Write a program that prompts the user to enter the center and a point on the circle (two tuples containing an x and y value).
#The program should then output the circle’s radius, diameter, circumference, and area. 
def validate_input(prompt):
  tuple_userInput = ()
  while True:
    userInput = input(prompt).split()
    #print(len(userInput))
    if len(userInput) != 2:
      print("Input lenght: " + str(len(userInput)) + "\nInvalid Input!!! Requires 2 values")
    elif len(userInput) == 2:
      try:
          x = float(userInput[0])
          y = float(userInput[1])
          tuple_userInput = (x, y)
          return tuple_userInput
      except ValueError:
          print("Invalid Input!!! Only numbers are allowed")

#REQUIREMENT: Your program must have at least the following functions:
#TO-DO: calculateRadius: 
  #Receives the x-y coordinates of the center and point on the circle (as input by the user)
  #calculates the distance between the points.
  #This value is returned as the radius of the circle.
def calculateRadius(center, apoint):
  #Center coordinate
  x1 = abs(center[0])
  y1 = abs(center[1])
  
  #A point coordinate
  x2 = abs(a_point[0])
  y2 = abs(a_point[1])

  r = round(math.sqrt(pow(x2-x1,2) + pow(y2-y1,2)),3) #d = sqrt(x2−x1)^2 + (y2−y1)^2)
  
  return r  

#TO-DO: calculateArea: 
    #Receives the radius of a circle
    #calculates and returns the area of the circle.
def calculateArea(radius):
  area = round(math.pi * pow(radius,2),3) # math.pi * radius**2
  return area


#TO-DO: calculatePerimeter: 
    #Receives the radius of a circle
    #calculates and returns the perimeter of the circle.
def calculatePerimeter(radius):
  perimeter = round(2 * math.pi * radius,3)
  return perimeter


#TO-DO: The output should clearly display the radius, area, and perimeter of the resulting circle.
center_point = validate_input("\nPlease enter x-y values for center point of a circle: "+\
                              "\n" + "Example: 1 2" +\
                              "\n" + "Your input: ")
a_point = validate_input("\nPlease enter x-y values for a point on a circle: "+\
                         "\n" + "Example: 1 2" +\
                         "\n" + "Your input: ")

radius = calculateRadius(center_point, a_point)
area = calculateArea(radius)
perimeter = calculatePerimeter(radius)

print("\nCenter point:       \t", center_point,\
      "\nA point on a circle:\t", a_point)

print("\nThe radius is:   \t"+ str(radius) +\
      "\nThe area is:     \t" + str(area) +\
      "\nThe perimeter is:\t" + str(perimeter))



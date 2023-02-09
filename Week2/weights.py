#Author: Vinh Tran
#Course: COMPPYE1-01A-A6-102230-TR-WE1
#Date: 01/19/2023
#Program name: Weight on Other Planets
#Description:
#  Design a Python program that asks a user for their name and weight.
#  The program will greet the user by name and then calculate/display the user's weight on the other planets.
#  Each item should be displayed on a line by itself.

# Use the following values for the conversions

# Body    Multiple of Earth’s Gravity
# Sun     27.01
# Mercury 0.38
# Venus   0.91
# Earth   1 (defined)
# Moon    0.166
# Mars    0.38
# Jupiter 2.34
# Saturn  1.06
# Uranus  0.92
# Neptune 1.19
# Pluto   0.06
#
#
#
import math

print("Calculate human weight on different planet")

name = input("What is your name?\n")
weight = float(input("What is your weight?\n"))

p_weight={"Sun":27.01,
          "Mercury":0.38,
          "Venus":0.91,
          "Earth" :1,
          "Moon" :0.166,
          "Mars" :0.38,
          "Jupiter" :2.34,
          "Saturn" :1.06,
          "Uranus" :0.92,
          "Neptune" :1.19,
          "Pluto":0.06}


#print(p_weight[0].values())
print("\nHi",name,"\n")
print("Here is the list of your weight will be in different planets:")

for planet,gravity in p_weight.items():
  calWeight = weight * gravity  
  print(planet,round(calWeight,3))
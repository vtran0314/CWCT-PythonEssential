################################
# Program name: falling_distance.py

#  Author: Vinh Tran
#  Course: Python Essentials
#  Date: 8/2/2023
#  Assignment: Module 4 - Falling Distance
#  Purpose: Calculate falling distance of an object base on given time
########################################


gravity = 9.8
distance = 0 # Fall distance: d = 1/2 gt^2
def get_user_input(prompt):
    while True:
        try:
            userInput=int(input(prompt))
            assert userInput > 0 #Test if its true

        except AssertionError:
            print("Time must be great than zero and are only positive number!!!\n")
        
        except:
            print("Invalid input!!! A whole number only")

        else:
            return userInput
            break

def fallingDistance(sec):
  print("Time(s)\t Distance(m)\n")
  if sec <= 5:
    for s in range(0, sec+1):
      d = 0.5 * gravity * pow(s,2)
      print(str(s)+"s \t"+str(round(d))+"m")
  else:
    for s in range(0, sec, 5):
      d = 0.5 * gravity * pow(s,2)
      print(str(s)+"s \t"+str(round(d))+"m")
    
    #Include the last increment and print to screen
    d = 0.5 * gravity * pow(sec,2)
    print(str(sec)+"s \t"+str(round(d))+"m")


sec = int(get_user_input("Please input an object falling's time: "))
fallingDistance(sec)
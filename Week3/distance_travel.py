################################
# Program name: distance_travel.py
#  Author: Vinh Tran
#  Course: Python Essentials
#  Date: 1/31/2023
#  Assignment: Module 3 - Distance Traveled
#  Purpose:
#   A program that asks the user for the speed of a vehicle (in miles per hour) and how many hours it has traveled. 
#   The program then display the distance the vehicle has traveled for each hour of that time period.
#
########################################

def speed_validation(prompt):
    while True:
        try:
            userInput=int(input(prompt))
            if userInput > 100:
                print("LOL you are racing!!!")
            assert userInput > 0 #Test if its true    
        except AssertionError:
            print("Invalid input, try again\n")

        except:
            print("Input cannot be non-numeric character")

        else:
            return userInput
            break


def time_validation(prompt):
    while True:
        try:
            userInput=int(input(prompt))
            assert userInput > 0 #Test if its true
            
        except AssertionError:
            print("Invalid input, try again\n")
        
        except:
            print("Input cannot be non-numeric character")

        else:
            return userInput
            break

speed = speed_validation("What is the speed of the vehicle in mph? ")

time = time_validation("How many hours has it traveled? ")


print('''
Hour  Distance Traveled
--------------------------------''')
for i in range(time+1):
    print(str(i) + "\t" + str(speed*i))




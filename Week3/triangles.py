################################
# Program name: triangles.py

#  Author: Vinh Tran
#  Course: Python Essentials
#  Date: 1/31/2023
#  Assignment: Module 3 - Triangles
#  Purpose: 
#     A program that prompts the user to enter the lengths of three sides of a triangle. 
#     The program will output a message indicating:
#         whether or not the lengths form a triangle and, if so,
#         whether or not the triangle is a right triangle,
#         an isosceles triangle, and/or 
#         an equilateral triangle.
########################################


def get_number_input(prompt):
    while True:
        try:
            userInput=float(input(prompt))
            assert userInput > 0 #Test if its true

        except AssertionError:
            print("Lenghts must be great than zero and are only positive number!!!\n")
        
        except:
            print("Invalid input!")

        else:
            return userInput
            break

def triangle_types(a,b,c):
    if a == b == c:
        print("this is an equilateral triangle")

    elif a == b or a == c or b == c:
        print("this is an isosceles triangle")

    elif (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        print("this is a right triangle")

    else:
        print("this is a triangle")
    
    
print('''
Triangles program
Purpose: 
     Enter the lengths of three sides of a triangle and I will let you know:
         whether or not the lengths form a triangle and, if so, 
         whether or not the triangle is a right triangle,
         an isosceles triangle, and/or 
         an equilateral triangle.
''')
        
ORDINALS = ('1st','2nd','3rd')
fmt = 'Enter {} length: \n'

a, b, c = [get_number_input(fmt.format(o)) for o in ORDINALS]

triangle_types(a,b,c)

#print(a,b,c)


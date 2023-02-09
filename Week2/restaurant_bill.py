#Author: Vinh Tran
#Course: Python Essential
#Date: 01/19/2023
#Program name: Restaurant Bill
#Description:
  # Write a Python script that informs a user of their total meal charges. 

  # Prompt the user for the amount of the meal (e.g. $32.95).
  # Compute the tax on the restaurant bill. The tax should be 6.75 percent of the meal cost. 
  # Prompt the user for the tip amount (Suggesting a value equal to 18 percent of the total).
  # Display the meal cost, tax amount, tip amount, and total bill on the screen.
import math

totalMeal= 32.95
tax = totalMeal * 0.0675
suggestTip = totalMeal * 0.18

print("Recipe")
print("Total meal:", totalMeal, "\nTax:",tax)
print("\nSuggest Tip:", suggestTip)

Tip = float(input("Please input your tip: "))
totalBill = totalMeal + tax + Tip

print("\nTotal:", totalBill)

"""
A script to show off the creation and use of objects.

Author: Charles Smith
Date: 08 January 2021
"""
import introcs
import funcs


# Step 1: Create a green RGB object, assign it to variable green, and then print it
# Step 2: Create a 50% transparent red RGB object, assign it to variable red, and print it
# Step 3: Call the function blend on red/green, assign it to variable brown, and print it
# Step 4: Call the function blendUnder on green/red, and then print variable green
green = introcs.RGB(0,255,0,255)
print(green)
red = introcs.RGB(255,0,0,128)
print(red)
brown = funcs.blend(red,green)
print(brown)
funcs.blendUnder(green,red)
print(green)

import math
from datetime import datetime


current_date_and_time = datetime.now()
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume1 = width*aspect + 2540 * diameter
volume2 = math.pi * width**2 * aspect * volume1
volume = volume2 / 10000000000
print()
print(f"The approximate volume is {volume:.2f} liters")
buy = input("Would you like to buy the tire?(yes,no)")
if buy == 'yes':
    nu = input("What is your phone number? ")
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {nu}",file=volumes_file)
else:
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}",file=volumes_file)
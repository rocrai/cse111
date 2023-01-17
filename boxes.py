import math
total = int(input("Enter the number of items: "))
items = int(input("Enter the number of items per box: "))

box = total / items

print(f"For {total} items, packing {items} items in each box, you will need {math.ceil(box)} boxes.")



from datetime import datetime
subtotal = float(input("Please enter the subtotal: "))
 
subtotaltax = subtotal * 0.06
total = subtotaltax + subtotal

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50:
    discount = subtotal * .10
    subtotal -= discount
    subtotaltax = subtotal * 0.06
    subtotal += subtotaltax
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {subtotaltax:.2f}")
    print(f"Total: {subtotal:.2f}")
else:
    subtotaltax = subtotal * 0.06
    total = subtotaltax + subtotal
    print(f"Sales tax amount: {subtotaltax:.2f}")
    total = subtotaltax + subtotal
    print(f"Total: {total:.2f}")


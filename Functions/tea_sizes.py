# You sell different sizes of tea.
# Instead of writing down formulas everywhere, create a function.
# Tasks:
# 1. Write calculate_bill(cups, price_per_cup)
# 2. Return total bill 
# 3. Use this function for multiple orders

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3, 15)
print(my_bill)

#ou
print("Order for table 2: ", calculate_bill(2, 50))
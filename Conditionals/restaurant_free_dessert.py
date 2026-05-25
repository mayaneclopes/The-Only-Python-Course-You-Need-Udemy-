# Restaurant Billing System
# You’re designing a billing system for a restaurant. 
# Depending on the total bill amount entered by the customer, they might get a free dessert.
# Tasks:
# If the bill amount is greater than 500, return the string "You get a free dessert!"
# Otherwise, return the string: "No free dessert this time."

def get_delivery_offer(bill_amount: float) -> str:
    # Write your code below this line
    if bill_amount > 500:
        return "You get a free dessert!"
    else:
        return "No free dessert this time."
    pass
def process_order(item, quantity):
    try:
        price = {"chicken": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that dish is not on menu")
    except TypeError:
        print("Quantity must be a number")

process_order("beef", 2)
process_order("chicken", "two")
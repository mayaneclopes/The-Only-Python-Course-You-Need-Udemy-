class InvalidFoodError(Exception): pass

def bill(flavor, dishes):
    menu = {"chicken": 20, "beef": 40}
    try:
        if flavor not in menu:
            raise InvalidFoodError("That flavor is not available")
        if not isinstance(dishes, int):
            raise TypeError("Number of dishes must be an integer")
        total = menu[flavor] * dishes
        print(f"Your bill for {dishes} dishes of {flavor}: {total} dolars")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting!")

bill("fish", 2)
bill("chicken", "two")
bill("beef", 2)
class OutOfIngredientsError(Exception):
    pass

def make_food(rice, beans):
    if rice == 0 or beans == 0:
        raise OutOfIngredientsError("Out of rice or beans")
    print("food is ready")

make_food(0, 1)
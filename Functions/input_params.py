
# def make_tea(tea, milk, sugar)
#     print(tea, milk, tea)

# make_tea("Ginger", "Yes", "Low") #positional 
# make_tea(tea="Green", sugar="Medium", milk="No") #keywords

def special_tea(*args, **kwargs):
    print("Ingredients", args)
    print("Extras", kwargs)

special_tea("Cinnamon", "Cardamom", sweetner="Honey", foam="Yes")

def tea_order(order=None):
    if order is None:
        order = []
    print(order)

tea_order()
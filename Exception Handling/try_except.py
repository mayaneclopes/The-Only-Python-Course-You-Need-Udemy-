food_menu = {"PF galinha": 30, "PF boi": 40}

try:
    food_menu["PF Peixe"]
except KeyError:
    print("The key you're trying to access does not exist")


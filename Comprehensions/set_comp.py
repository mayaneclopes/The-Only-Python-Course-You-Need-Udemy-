favorites = [
    "Lemon",
    "Pearl",
    "Melon",
    "Apple",
    "Lemon",
    "Melon"
]

unique = {fruit for fruit in favorites}
print(unique)

recipes = {
    "Chicken": ["rice", "beans", "chicken"],
    "Beef": ["rice", "beans", "beef"],
    "Tuna": ["rice", "beans", "tuna", "salad"],
}

unique_ingredients = {food for ingredients in recipes.values() for
                      food in ingredients}

print(unique_ingredients)
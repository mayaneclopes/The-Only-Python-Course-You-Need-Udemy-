def cook_food(flavor):
   if flavor not in ["chicken", "beef", "fish"]:
      raise ValueError("Unlisted flavor")
   print(f"Cooking {flavor} dish")

cook_food("veg")
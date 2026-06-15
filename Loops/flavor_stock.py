# Some chai flavors are out of stock.
# You want to skip those and stop entirely if someone
# requests a restricted flavor.
# Tasks:
# 1. Skip flavor that is out of stock
# 2. Break if flavor is discontinued

flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavors:
    if flavor == "Out of Stock":
        continue 
    if flavor == "Discontinued":
        break
    print("Discontinued item found")
     
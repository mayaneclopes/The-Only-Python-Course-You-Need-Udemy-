food_price_inr = {
    "Chicken": 40,
    "Beef": 50,
    "Tuna": 100
}

food_prices_usd = {food:price for food, price in food_price_inr.items()}
print(food_prices_usd)
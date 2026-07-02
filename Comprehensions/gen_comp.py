daily_sales = [5, 12, 10, 15, 5, 6, 3, 1]

total = sum(sale for sale in daily_sales if sale > 5)

print(total)
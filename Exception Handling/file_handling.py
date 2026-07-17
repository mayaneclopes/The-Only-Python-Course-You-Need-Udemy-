# file = open("order.txt", "w")
# try:
#     file.write("Chicken dish - 2 plates")
# finally: 
#     file.close()

with open("order.txt", "w") as file:
    file.write("Beef dish - 4 plates")
def serve_tea():
    tea_type = "Ginger" #local scope
    print(f"Inside function {tea_type}")

tea_type = "Lemon"
serve_tea()
print(f"Outside function: {tea_type}")

def tea_counter():
    tea_order = "Lemon" #Enclosing scope
    def print_order():
        tea_order = "Ginger"
        print("Inner:", tea_order)
    print_order()
    print("Outer: ", tea_order)

tea_order = "Camomila" #global
tea_counter()
print("Global: ", tea_order)
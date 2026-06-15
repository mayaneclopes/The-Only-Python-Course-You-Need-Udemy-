def update_order():
    tea_type = "Hortela"
    def kitchen():
        nonlocal tea_type
        tea_type = "Erva doce"
    kitchen()
    print("After kitchen update", tea_type)

update_order()


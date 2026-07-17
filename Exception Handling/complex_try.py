def serve_food(flavor):
    try:
        print(f"Preparing {flavor} PF")
        if flavor == "unknown":
            raise ValueError("We don't have that flavor")
    except ValueError as e:
        print("Error: ", e)
    else: 
        print(f"{flavor} PF is served")
    finally:
        print("Next customer please")

serve_food("Chicken")
serve_food("unknown")
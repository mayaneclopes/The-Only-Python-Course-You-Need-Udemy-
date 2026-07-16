class FoodOrder:
    def __init__(self, food_type, spiceness, size):
        self.food_type = food_type
        self.spiceness = spiceness
        self.size = size
    def __str__(self):
        return f"Pedido: {self.food_type} | Pimenta: {self.spiceness} | Tamanho: {self.size}"

    @classmethod 
    def from_dict(cls, order_data):
        return cls(
            order_data["food_type"],
            order_data["spiceness"],
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order_string):
        food_type, spiceness, size = order_string.split("-")
        return cls(food_type, spiceness, size)
    
class KitchenUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    
order1 = FoodOrder.from_dict({"food_type": "Brazilian",
                              "spiceness":"Hot",
                              "size":"large"})

order2 = FoodOrder.from_string("Greek-Low-Small")

print(order1)
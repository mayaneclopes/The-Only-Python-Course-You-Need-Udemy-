class Food:
    def __init__(self, type_, temperature):
        self.type = type_
        self.temperature = temperature

# class BrazilianFood(Food):
#     def __init__(self, type_, temperature, spice_level):
#         self.type = type_
#         self.temperature = temperature
#         self.spice_level = spice_level

# class BrazilianFood(Food):
#     def __init__(self, type_, temperature):
#        Food.__init__(self, type_, temperature)
#        self.temperature = temperature

class BrazilianFood(Food):
    def __init__(self, type_, temperature):
        super().__init__(type_, temperature) #super calls (Food)
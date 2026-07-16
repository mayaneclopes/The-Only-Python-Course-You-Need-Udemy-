class KitchenUtils:

    @staticmethod #decorator
    def clean_tools(text):
        return [item.strip() for item in text.split(",")]


raw = "  water , milk     , ginger,honey"

print(raw)
obj = KitchenUtils()
cleaned = KitchenUtils.clean_tools(raw)
print(cleaned)
tea_type = "Plain"

def front_desk():
    def kitchen():
        global tea_type
        tea_type = "Seis Ervas"
    kitchen()

front_desk()
print("Final global tea: ", tea_type)
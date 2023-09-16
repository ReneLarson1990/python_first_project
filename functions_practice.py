def hello():
    print("Hello, user!")

def pack(Fallout4, skyrim, starfield):
    return [Fallout4, skyrim, starfield]

def eat_lunch(lunch_items):
    lunch_items = ["fritos", "cheetos", "doritos"]
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")


hello()
result = pack("Fallout 4", "Skyrim", "Starfield")
print(result)
eat_lunch([])  



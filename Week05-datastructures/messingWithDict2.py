# Messing with Dictionary2
# Examples of For Loops in dictionaries
# Author: Andrea Cignoni

car = {
    "make": "Fiat",
    "model": "Punto",
    "price": 1000,
    "tags" :["pre-owned", "Best Buy", "Dealer"]
}

# print (car)

#   print (key, 'has value', car[key])

for key, value in car.items():
    print (key, "has a value", value)

import json


products : dict= {}
with open("products.json", "r") as file:
    data = json.load(file)

    for value in data:
        products[value["id"]]= value
        #print(products)

# print(products)

def save():
    with open ("products.json", "w") as file:
        json.dump(list(products.values()), file)

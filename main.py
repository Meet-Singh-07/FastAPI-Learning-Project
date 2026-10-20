from typing import Any

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18},
    1003: {"name": "USB-C Hub", "price": 29.99, "stock": 35},
    1004: {"name": "Laptop Stand", "price": 39.99, "stock": 12},
    1005: {"name": "Webcam", "price": 54.99, "stock": 25},
    1006: {"name": "Bluetooth Speaker", "price": 44.99, "stock": 30},
    1007: {"name": "External SSD", "price": 89.99, "stock": 10},
}

@app.get("/product")
def get_product(id: int| None = None) -> dict[str, Any]:
    if not id:
        id = max(products.keys())
        return products[id]
    # Check whether the requested product exists
    if id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product with the given ID was not found!",
        )

    return products[id]


@app.get("/products/{field}")
def get_product_field(field :str , id :int) -> dict[str,Any]:
    if id not in products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product with the given ID was not found!",
            )    
    return {
            field: products[id][field]
        }


@app.post("/product")
def creat_new_data(name :str, price:float, stock: int)-> dict[str, Any]:
    if price <= 0:
        raise HTTPException(
            status_code= status.HTTP_406_NOT_ACCEPTABLE, 
            detail="Price must be greater than 0! ",
        )

    if stock < 0:
         raise HTTPException(
              status_code=status.HTTP_406_NOT_ACCEPTABLE,
              detail = "Stock can not be zero"
         )

    if name in [product["name"] for product in products.values()]:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Product with the given name already exists!",
        )
    
    new_id = max(products.keys()) + 1
    products[new_id]= {
        "name":name,
        "price": price,
        "stock":stock
     }
    return products[new_id]

@app.put("/products")
def update_product(id:int ,name: str, price:float, stock:int):
    if id not in products:
        raise HTTPException(
            status_code= status.HTTP_406_NOT_ACCEPTABLE,
            detail= "Invalid Id !"
        )
    product = products[id]

    product= {
        "name": name,
        "price": price,
        "stock":stock,}

    products[id]= product 
    return products[id] 

@app.patch("/products")
def update_product_field(id:int, body:dict[str,Any])-> dict[str, Any]:
    products[id].update(body)
    return products[id]

@app.delete("/product")
def delete_product(id:int):
    if id not in products:
            raise HTTPException(
                status_code= status.HTTP_406_NOT_ACCEPTABLE,
                detail= "Invalid Id !"
            )
    products.pop(id)
    return {"detail" : f"Item with id {id} delelted successfully."}
# Module 6 - Complete app with Pydantic schemas
# Run (from the m06 folder):  fastapi dev app/main.py
from fastapi import FastAPI, HTTPException, status

from schema.models import ProductCreate, ProductRead, ProductStatus, ProductUpdate

app = FastAPI()

products = {
    1001: {"name": "Wireless Mouse", "price": 18.99, "stock": 42, "warehouse": 1, "status": "active"},
    1002: {"name": "Mechanical Keyboard", "price": 64.99, "stock": 18, "warehouse": 2, "status": "active"},
    1003: {"name": "USB-C Hub", "price": 29.99, "stock": 35, "warehouse": 1, "status": "active"},
    1004: {"name": "Laptop Stand", "price": 39.99, "stock": 12, "warehouse": 3, "status": "low_stock"},
    1005: {"name": "Webcam", "price": 54.99, "stock": 25, "warehouse": 2, "status": "active"},
    1006: {"name": "Bluetooth Speaker", "price": 44.99, "stock": 30, "warehouse": 4, "status": "active"},
    1007: {"name": "External SSD", "price": 89.99, "stock": 10, "warehouse": 5, "status": "low_stock"},
}


# We return a plain dict, so the schema goes in response_model=
# (it validates the output AND hides keys that are not in the schema)
@app.get("/product", response_model=ProductRead)
def get_product(id: int):
    if id not in products:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")
    return products[id]


@app.post("/product")
def create_product(product: ProductCreate) -> dict[str, int]:
    new_id = max(products.keys()) + 1
    products[new_id] = {
        **product.model_dump(),          # model -> dict, then unpack
        "status": ProductStatus.active,
    }
    return {"id": new_id}


@app.patch("/product", response_model=ProductRead)
def update_product(id: int, body: ProductUpdate):
    if id not in products:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")

    # exclude_none=True -> only fields the client really sent
    data = body.model_dump(exclude_none=True)
    if not data:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No data provided to update")

    products[id].update(data)
    return products[id]


@app.delete("/product")
def delete_product(id: int) -> dict[str, str]:
    if id not in products:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")
    products.pop(id)
    return {"detail": f"Product with id #{id} is deleted!"}
# Module 6 - Complete app with Pydantic schemas
# Run (from the m06 folder):  fastapi dev app/main.py
from fastapi import FastAPI, HTTPException, status
from database import Database
from schema.models import ProductCreate, ProductRead, ProductUpdate

app = FastAPI()

db = Database()


# We return a plain dict, so the schema goes in response_model=
# (it validates the output AND hides keys that are not in the schema)
@app.get("/product", response_model=ProductRead)
def get_product(id: int):
    product = db.get(id)
    if  not product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")
    return product


@app.post("/product")
def create_product(data: ProductCreate) -> dict[str, int]:
    new_id = db.create(data)
    return {"id": new_id}

    


@app.patch("/product", response_model=ProductRead)
def update_product(id: int, body: ProductUpdate):
    updated= db.upadte(id, body)
    if updated is None:
        raise HTTPException(status.HTTP_100_CONTINUE, "Given id doesn't exist!")
    return updated


@app.delete("/product")
def delete_product(id: int) -> dict[str, str]:
    deleted = db.delete(id)
    if not deleted :
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Given id doesn't exist!")
    
    return {"detail": f"Product with id = {id} is deleted!"}
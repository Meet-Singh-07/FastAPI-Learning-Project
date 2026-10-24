import random
from enum import Enum

from pydantic import BaseModel, Field




# Shared fields live in ONE base class
class BaseProduct(BaseModel):
    name: str = Field(description="Product title", min_length=3, max_length=100)
    price: float = Field(description="Price in US dollars", gt=0, le=10_000)
    stock: int = Field(description="Units available", ge=0)
    


# Response when READING a product (adds status)
class ProductRead(BaseProduct):
    pass


# Request body when CREATING (client never sets status)
class ProductCreate(BaseProduct):
    pass


# Request body when UPDATING (every field optional -> partial update)
class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=3, max_length=100)
    price: float | None = Field(default=None, gt=0, le=10_000)
    stock: int | None = Field(default=None, ge=0)
    











# from enum import Enum
# import random

# from pydantic import BaseModel, Field

# def random_warehouse():
#      return random.randint(1,5)

# class ProductStatus(str, Enum):
#      active = "active"
#      low_stock = "low_stock"
#      out_of_stock = "out of stock"


# class BaseProduct(BaseModel):
#      name: str = Field(description= "Product Title", min_length=5, max_length= 20)
#      price: float = Field(description= "Product Price in USD", gt=0, le = 1000)
#      stock: int =  Field(description= " Units available in the warehouse", gt= 1)
#      warehouse : int = Field(description= "Warehouse Code(1-5)", default_factory=random_warehouse)
#     #  status : productStatus 

# class ProductCreate(BaseProduct):
#      pass 

# class ProductRead(BaseProduct):
#      status : ProductStatus

# class ProductUpdate(BaseModel):
#      name: str | None  = Field(
#           default = None,
#           description= "Product Title",
#           min_length=5,
#           max_length= 20)
#      price: float | None = Field(default = None,description= "Product Price in USD", gt=0, le = 1000)
#      stock: int | None=  Field(default = None,description= " Units available in the warehouse", gt= 1)
#      warehouse : int| None = Field(description= "Warehouse Code(1-5)", default= None)

from pydantic import BaseModel


class OrderResponse(BaseModel):
    total_price: int


class Item(BaseModel):
    name: str
    price: float
    quantity: int

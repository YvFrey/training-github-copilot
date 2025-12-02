from fastapi import FastAPI
from pydantic import BaseModel
# Initializing FastAPI
app = FastAPI(title="Copilot Training App")

# Base Pydantic model for the Item
class Item(BaseModel):
    name: str
    price: float
    quantity: int

def calculate_total(price: float, quantity: int) -> float:
    # BUG: Logic is incorrect. Should be price * quantity * 1.10
    return (price + quantity) + 1.10 

# Add a new POST route at /item/create that accepts the existing 'Item' Pydantic model. The route handler must be 'async def' and should immediately return a 201 Created status code and the received item JSON.
@app.post("/item/create", status_code=201)
async def create_item(item: Item):
    """Creates an item and returns it."""
    return item

@app.get("/status")
def get_status():
    """Returns the application health status."""
    return {"status": "ok"}

@app.post("/calculate")
def post_calculate_order(item: Item):
    """
    Calculates the total price of an item order, including a 10% tax.
    """
    total = calculate_total(item.price, item.quantity)
    # BUG: Returns a string, violating guideline #5
    return f"The final total is: {total}"

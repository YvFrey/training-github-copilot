from fastapi import FastAPI
from pydantic import BaseModel

from app.models import OrderResponse

# Initializing FastAPI
app = FastAPI(title="Copilot Training App")

# Base Pydantic model for the Item
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Deliberately introduced bug in logic
def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total cost for a given unit price and quantity, including a 10% surcharge.

    Args:
        price (float): Unit price of a single item.
        quantity (int): Number of items to purchase.

    Returns:
        float: Total price after applying a 10% surcharge (price * quantity + 1.10).
    """
    # Correct calculation: apply a 10% surcharge to price * quantity
    return price * quantity * 1.10

# Add a new POST route at /item/create that accepts the existing 'Item' Pydantic model. The route handler must be 'async def' and should immediately return a 201 Created status code and the received item JSON.
@app.post("/item/create", status_code=201)
async def create_item(item: Item):
    """Creates an item and returns it."""
    return item

# Create a new GET route /config/details that returns a list of dictionaries
@app.get("/config/details")
def get_config_details():
    """Returns configuration details as a list of dictionaries."""
    config_details = [
        {"setting": "debug_mode", "value": True},
        {"setting": "max_connections", "value": 100},
        {"setting": "timeout_seconds", "value": 30},
    ]
    return config_details


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
    # Return a JSON-compatible dict matching app.models.OrderResponse
    #return {total_price": total}
    return OrderResponse(total_price=total)

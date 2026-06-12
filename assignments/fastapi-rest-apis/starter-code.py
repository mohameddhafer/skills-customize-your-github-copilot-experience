from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI(title="Starter Items API")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# In-memory store for starter purposes
items: Dict[int, Item] = {}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Starter Items API"}


@app.get("/items")
async def list_items():
    return list(items.values())


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    item = items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
async def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items[item.id] = item
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("assignments.fastapi-rest-apis.starter-code:app", host="127.0.0.1", port=8000, reload=True)

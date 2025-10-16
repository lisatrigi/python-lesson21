from fastapi import FastAPI

app = FastAPI()
# @app.get("/")
# def home():
#     return{"message":"Hii"}

# @app.get("/user/{user_id}")
# def get_user(user_id: int):
#     return{"user_id":user_id, "name":"Lisa lisa"}

@app.get("/items/")
def read_items():
    return{"items":["item1","item2","item3"]}

@app.post("/items/")
def create_items(name:str,price:float):
    return{"item_name":name, "item_price": price}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return{"item_id":item_id, "name":name, "price":price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return{"item_id":f"item {item_id} deleted"}
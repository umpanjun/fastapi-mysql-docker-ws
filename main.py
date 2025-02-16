from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# เสิร์ฟโฟลเดอร์ static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Iphone16 Plus", "price": 55900, "image": "http://localhost:8001/static/images/iphone16.jpg"},
        {"id": 2, "name": "Samsung S25Ultra", "price": 50900, "image": "http://localhost:8001/static/images/s25ultra.jpg"},
        {"id": 3, "name": "IPhone 12", "price": 12900, "image": "http://localhost:8001/static/images/iphone12.jpg"}
    ]

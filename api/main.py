from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from product import get_all_products, get_product_by_id, create_product, update_product, delete_product
from product.models import ProductModel
from typing import List

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import Response

@app.post("/products", response_model=ProductModel, status_code=201)  # ✅ เพิ่ม status_code=201
async def create_new_product(product: ProductModel):
    try:
        product_id = create_product(product)
        response_data = ProductModel(id=product_id, name=product.name, description=product.description, price=product.price)
        
        print("✅ Response Data:", response_data.dict())  # Debugging
        
        return Response(content=response_data.json(), status_code=201, media_type="application/json")  # ✅ ส่ง JSON ที่ถูกต้อง
    except Exception as e:
        print("❌ Error in FastAPI:", str(e))
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/")
async def root():
    return {"message": "FastAPI is running"}

@app.get("/products", response_model=List[ProductModel])
async def read_products():
    try:
        return get_all_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/products/{product_id}", response_model=ProductModel)
async def read_product(product_id: int):
    try:
        return get_product_by_id(product_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/products", response_model=ProductModel)
async def create_new_product(product: ProductModel):
    try:
        product_id = create_product(product)
        return {**product.dict(), "id": product_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/products/{product_id}", response_model=ProductModel)
async def update_existing_product(product_id: int, product: ProductModel):
    try:
        update_product(product_id, product)
        return {**product.dict(), "id": product_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/products/{product_id}")
async def delete_existing_product(product_id: int):
    try:
        delete_product(product_id)
        return {"message": "Product deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

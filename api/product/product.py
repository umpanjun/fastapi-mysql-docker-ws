from fastapi import HTTPException,APIRouter
from database.query import query_get, query_create, query_update
from .models import ProductModel
from typing import List
from pydantic import BaseModel

class ProductModel(BaseModel):
    name: str
    description: str
    price: float

# ฟังก์ชันสำหรับดึงข้อมูลสินค้า
def get_all_products() -> List[ProductModel]:
    products = query_get("SELECT * FROM products", ())  # เปลี่ยน 'product' เป็น 'products'
    return products

def get_product_by_id(product_id: int) -> ProductModel:
    product = query_get("SELECT * FROM products WHERE id = %s", (product_id,))
    if not product:
        raise Exception("Product not found")
    return product[0]

def create_product(product: ProductModel) -> int:
    sql = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
    params = (product.name, product.description, product.price)
    return query_create(sql, params)

def update_product(product_id: int, product: ProductModel) -> bool:
    sql = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"
    params = (product.name, product.description, product.price, product_id)
    return query_update(sql, params)

def delete_product(product_id: int) -> bool:
    sql = "DELETE FROM products WHERE id = %s"
    return query_update(sql, (product_id,))

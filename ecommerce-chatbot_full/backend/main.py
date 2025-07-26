from fastapi import FastAPI
from database import products, orders

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the E-commerce Chatbot API"}

@app.get("/top-products")
def get_top_products():
    top = products.sort_values(by="units_sold", ascending=False).head(5)
    return top.to_dict(orient="records")

@app.get("/order-status/{order_id}")
def get_order_status(order_id: int):
    order = orders[orders["order_id"] == order_id]
    if order.empty:
        return {"error": "Order not found"}
    return order.to_dict(orient="records")[0]

@app.get("/stock/{product_name}")
def get_stock(product_name: str):
    product = products[products["product_name"].str.lower() == product_name.lower()]
    if product.empty:
        return {"error": "Product not found"}
    return {"product": product_name, "stock": int(product["stock"].values[0])}

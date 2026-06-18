from fastapi import FastAPI , HTTPException

from service.product import get_all_products



app = FastAPI()

@app.get('/')

def root():
    return {"message":"welcome to fastAPI"}


@app.get('/products')

def get_products():
    # products=["Brush","Laptop","Mouse","Moniter"]
    return get_all_products()



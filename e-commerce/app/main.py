from fastapi import FastAPI , HTTPException, Query

from service.product import get_all_products



app = FastAPI()

@app.get('/')

def root():
    return {"message":"welcome to fastAPI"}


# @app.get('/products')

# def get_products():
#     # products=["Brush","Laptop","Mouse","Moniter"]
#     return get_all_products()


@app.get("/products")

def list_products(name:str = Query(default=None,
                                min_length=1,
                                max_length=50,
                                description="Search by product name(case insensitive)")
                ,
                sort_by_price: bool = Query(default=False, description="Sort products by price"),
                order: str = Query(default="asc",description="Sort order when sort_by_price=true(asc,desc)")
                ):
    products = get_all_products()
    
    
    if name:
        needle = name.strip().lower()
        products = [p for p in products if needle in p.get("name","").lower()]
        
        if not products:
            
            raise HTTPException(status_code=404,detail=f"No product found matching name={name}")
        
        total= len(products)
        
        if sort_by_price:
            reverse= order =="desc"
            product = sorted(products,key=lambda p:p.get("price",0),reverse=reverse)
        
    return {
        "total": total,
        "items": products
    }
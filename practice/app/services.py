from db import engine
from tables import categories, products
from sqlalchemy import insert, select, update, delete, asc
from pydantic import BaseModel # type: ignore

class Product(BaseModel):
  name: str
  desc: str
  price: int
  category_id: int


# ========== Category ==========
def create_category(name: str):
  with engine.connect() as conn:
    new_cate = insert(categories).values(name=name)
    result = conn.execute(new_cate)
    conn.commit()
    return result

def get_categories():
  with engine.connect() as conn:
    all_cate = select(categories)
    result = conn.execute(all_cate).fetchall()
    return result

def get_category_by_id(category_id: int):
  with engine.connect() as conn:
    cate = select(categories).where(categories.c.id == category_id)
    result = conn.execute(cate).first()
    return result

def update_category_by_name(category_id: int, name: str):
  with engine.connect() as conn:
    update_cate = update(categories).where(categories.c.id == category_id).values(name=name)
    conn.execute(update_cate)
    conn.commit()

def delete_category_by_id(category_id):
  with engine.connect() as conn:
    delete_cate = delete(categories).where(categories.c.id == category_id)
    conn.execute(delete_cate)
    conn.commit()

# ========== Product ==========
def create_product(name: str, desc: str, price: int, category_id: int):
  with engine.connect() as conn:
    new_product = insert(products).values(name=name, desc=desc, price=price, category_id=category_id)
    result = conn.execute(new_product)
    conn.commit()
    return result

def get_products():
  with engine.connect() as conn:
    all_products = select(products).order_by(asc(products.c.name))
    results = conn.execute(all_products).fetchall()
    return results

def get_product_by_id(product_id: int):
  with engine.connect() as conn:
    product = select(products).where(products.c.id == product_id)
    result = conn.execute(product).first()
    return result

def get_products_by_cate_id(category_id: int):
  with engine.connect() as conn:
    product = select(products).where(products.c.category_id == category_id)
    result = conn.execute(product).fetchall()
    return result

def update_product(product_id: int, new_data: Product):
    with engine.begin() as conn:
      stmt = update(products).where(products.c.id == product_id).values(
              name=new_data.name,
              desc=new_data.desc,
              price=new_data.price,
              category_id=new_data.category_id
            )
      result = conn.execute(stmt)
      return result.rowcount

def delete_product_by_id(product_id):
  with engine.connect() as conn:
    delete_product = delete(products).where(products.c.id == product_id)
    conn.execute(delete_product)
    conn.commit()

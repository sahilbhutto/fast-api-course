from tables import create_tables
from services import *

# Create Tables
create_tables()

# ============== Category Operations ==============

# create_category("Fruits")
# create_category("Vegetables")
# create_category("Mobiles")

# categories = get_categories()
# print(f"All Categories = {categories}")

# category = get_category_by_id(1)
# print(f"Category = {category}")

# update_category_by_name(3, "Phones")

# delete_category_by_id(3)


# ============== Products Operations ==============

# create_product("Apple", "This is sweat apples", 25.45, 1)
# create_product("Banana", "This is session bana", 20.12, 1)
# create_product("Potatoes", "Sweat potatoes with better taste", 12.00, 2)
# create_product("Tomatoes", "Tasty tomatoes & sessional", 18.00, 2)
# create_product("Orange", "Modern oranges here", 20.00, 1)

# products = get_products()
# print(f"All Products = {products}")

# product = get_product_by_id(1)
# print(f"Product by ID = {product}")

# product = get_products_by_cate_id(1)
# print(f"Product by Cate ID = {product}")

# result = update_product(
#     1,
#     Product(
#         name= "Apples",
#         desc= "World best fruits",
#         price= 25.00,
#         category_id= 1
#     )
# )
# print(f"Updated Product = {result}")

# delete_product_by_id(4)

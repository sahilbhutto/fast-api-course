from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
from db import engine

metadata = MetaData()

# Category Table
categories = Table(
  "categories",
  metadata,
  Column("id", Integer, nullable=False, primary_key=True),
  Column("name", String(length=30), nullable=False, unique=True),
)

# Products Table
products = Table(
  "products",
  metadata,
  Column("id", Integer, nullable=False, primary_key=True),
  Column("name", String(length=40), nullable=False),
  Column("desc", String(length=200), nullable=False),
  Column("price", Integer, nullable=False),
  Column("category_id", Integer, ForeignKey("categories.id"), nullable=False)
)

# Create Tables
def create_tables():
  metadata.create_all(engine)

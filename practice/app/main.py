from fastapi import FastAPI, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Reviewer(BaseModel):
  username: str = Field(min_length=3)
  email: EmailStr


class Review(BaseModel):
  product_name: str = Field(min_length=3, max_length=50)
  rating: int = Field(min=1, max=5)
  comment: str = Field(min_length=10, max_length=100)
  is_verified: bool = False
  reviewer: Reviewer

@app.post("/reviews", status_code=status.HTTP_201_CREATED)
async def create_reviews(review: Review):
  return review

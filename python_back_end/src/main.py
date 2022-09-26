from typing import Union

from fastapi import FastAPI
from src.settings import Settings
from src.recipes_finder import RecipesFinder

settings = Settings()
finder = RecipesFinder(settings.SOLR_URL)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health_check")
def read_root():
    return "we are in business."

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/recipes")
def read_item(ingredients: Union[str, None] = None):
    response = finder.get_recipes(ingredients)
    return response
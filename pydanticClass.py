from pydantic import BaseModel

class Recipe(BaseModel):
    title:str
    calories:int

dal=Recipe(title="yellow dal",calories=25)
print(f"Recipe name is {dal.title} having calories {dal.calories}")
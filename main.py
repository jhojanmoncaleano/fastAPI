#se importan las librerias segun el uso, ejemplo  se importa de ultimo fasApi porque funciona ensima de pydantic y asi sucesivamente.Se tiene que respetar siempre el orden para tener el codigo de manera limpia




#python
from typing import Optional
from fastapi.param_functions import Query
from enum import Enum

#pydantic
from pydantic import BaseModel
from pydantic import Field

# fastApi
from fastapi import FastAPI, applications
from fastapi import Body, Query, Path


app = FastAPI()

#models
class HairColor(Enum):
    white= "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class location(BaseModel):
    city:str
    state:str
    country:str

class person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example= "alejandra"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example= "martinez"
    )
    age:int = Field(
        ...,
        gt=0,
        le=115,
        example=22
    )
    hair_color:Optional[HairColor] = Field (default=None, example= "red")
    is_married: Optional[bool]= Field(default=None, example=True)
#Ejemplos automaticos ----->
    # class Config:
    #     schema_extra= {
    #         "example": {
    #             "frist_name": "jhojan",
    #             "last_name":" Stiven moncaleano",
    #             "age": 23,
    #             "hair_color": "black",
    #             "is_married": False
    #         }
    #     }


@app.get("/")
def home():
    return {"hello": "world!!!!"}

    # request and response body


@app.post("/person/new")
def create_person(person: person = Body(...)):
    return person


# validaciones query parametrems

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1, 
        max_length=50),
        title= "person name",
        description="this is the person name. its between 1 and 50 characteres",
        example= "Maria",
    age: Optional[str] = Query(
        ...,
        title= "Person age",
        description="this is the person age. its required",
        example= 24
        )
):
    return{name:age}


#validaciones : path parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id : int = Path(
        ...,
        gt=0,
        example= 123
        )
):

    return {person_id: "It exist !"}


    #Validaciones: request boy




@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
         ...,
        title= "person ID",
        description= "this is person id",
        gt=0,
        example= 123
    ),
    person: person = Body(...),
    # location: location = Body(...),

):
    # results = person.dict()
    # results.update(location.dict())
    # return person

    return person 
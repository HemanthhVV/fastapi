from enum import Enum
from pydantic import BaseModel
from datetime import date

## Suppose What if the user provide non useful info
## Aport from specific fields
## For this we can use the Enum class to make use of some validation

class generalizeMarkets(Enum):
    FINANCE = "finance"
    HEALTHCARE = "healthcare"
    TECH = "tech"
    CLEANING = "cleaning"

class Product(BaseModel):
    product_name:str
    launch_date:date

class Company(BaseModel):
    id:int
    name:str
    company_market:str
    products : list[Product] = [] ## Default value is empty list
    ##  It means , if there is no product under a company , it will return an empty list

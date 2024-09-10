from enum import Enum
from pydantic import BaseModel,field_validator
from datetime import date

## Suppose What if the user provide non useful info
## Aport from specific fields
## For this we can use the Enum class to make use of some validation

class generalizeURLMarkets(Enum):
    FINANCE = "finance"
    HEALTHCARE = "healthcare"
    TECH = "tech"
    CLEANING = "cleaning"
    FOOD = "food"

class generalizeMarkets(Enum):
    FINANCE = "Finance"
    HEALTHCARE = "Healthcare"
    TECH = "Tech"
    CLEANING = "Cleaning"
    FOOD = "Food"


class Product(BaseModel):
    product_name:str
    launch_date:date

class CompanyBaseModel(BaseModel):
    name:str
    company_market: generalizeMarkets
    products : list[Product] = []
    ## Default value is empty list
    ##  It means , if there is no product under a company , it will return an empty list


class CompanyCreate(CompanyBaseModel):
    company_market: generalizeMarkets
    ## Defining the validator(pre-validator here to get the data in the Title cased format)
    @field_validator('company_market',mode='before')
    @classmethod
    def make_genre_titled(cls,value:str):
        if not('A' <= value[0] <= 'Z') : 
            print(
            "Not titled case, converting to titled case"
            )
        return value.title()

    

class CompanyWithId(CompanyBaseModel):
    id:int
from fastapi import FastAPI, HTTPException
from schemas import generalizeURLMarkets, CompanyCreate, CompanyBaseModel, CompanyWithId
from datetime import date

app = FastAPI()

## This is an simple endpoints on idea that
## how the fastapi is working



# prepare the example dict
companies = [
    {"id": 1, "name": "abc", "company_market": "Cleaning"},
    {"id": 2, "name": "def", "company_market": "Tech"},
    {"id": 3, "name": "ghi", "company_market": "Finance"},
    {"id": 4, "name": "jkl", "company_market": "Healthcare"},
    {"id": 5, "name": "mno", "company_market": "Cleaning"},
    {"id": 6, "name": "pqr", "company_market": "Finance",
     "products": [
         {
             "product_name": "Finance_bot",
             "launch_date": "2024-11-11"
         },
     ]
     },
    {"id": 7, "name": "stu", "company_market": "Tech"},
    {"id": 8, "name": "vwx", "company_market": "Tech"},
    {"id": 9, "name": "yz", "company_market": "Healthcare"},
    {"id": 10, "name": "abc123", "company_market": "Finance"},
    {"id": 11, "name": "xz", "company_market": "Cleaning"}
]




@app.get('/')
async def index() -> dict[str, str]:
    ## Also we are mention the return type of the api request
    ## Which helps in the data validation for response
    return {
        "hello": "Universe"
    }
    ## If the return type varies from the mentioned return type on the function , it will raise an exception




@app.get('/companies', response_description="Companies fetched successfully")
## Query parameter -> which are the parameters defined inside the function ,
## rather then in the path (Path Parameter)
async def bands(market: generalizeURLMarkets | None = None, products_available: bool = False) -> list[CompanyWithId]:
    company_array =[CompanyWithId(**c) for c in companies]
    if market and products_available:
        return [
            c for c in company_array if c.company_market.value.lower() == market.value and c.products
        ]
    if market:
        return [
            c for c in company_array if c.company_market.value.lower() == market.value
        ]
    return company_array





@app.get("/companies/{company_id}")
async def get_Company_details(company_id: int) -> list[CompanyWithId]:
    ## The purposes of the next is to retrive the first match
    ## We can also retain this with comprehsion, but the next() is more efficient
    ## also Hide all the iteration working behind
    details = next((CompanyWithId(**c) for c in companies if c["id"] == company_id), None)
    if details:
        return [
            details
        ]
    raise HTTPException(status_code=404, detail="No company found")





## Understanding the path parameter
@app.get('/companies/market/{market}')
async def get_Market_based_company(market: generalizeURLMarkets) -> list[CompanyWithId]:
    return [
        CompanyWithId(**c) for c in companies if c["company_market"].value.lower() == market.value
    ]





@app.post('/companies')
async def create_company(company_data:CompanyCreate)->CompanyWithId:
    id = companies[-1]["id"] + 1
    company = CompanyWithId(id = id , **company_data.model_dump()).model_dump()
    companies.append(company)
    return company
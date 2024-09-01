from fastapi import FastAPI,HTTPException
from schemas import Company,generalizeMarkets
from datetime import date
app = FastAPI()

## This is an simple endpoints on idea that
## how the fastapi is working

# prepare the example dict
companies = [
    {"id": 1, "name": "abc", "company_market": "cleaning"},
    {"id": 2, "name": "def", "company_market": "tech"},
    {"id": 3, "name": "ghi", "company_market": "finance"},
    {"id": 4, "name": "jkl", "company_market": "healthcare"},
    {"id": 5, "name": "mno", "company_market": "cleaning"},
    {"id": 6, "name": "pqr", "company_market": "finance",
         "productss":[
             {
            "product_name":"finance_bot",
            "launch_date":"2024-11-11"
            }
        ]
     },
    {"id": 7, "name": "stu", "company_market": "tech"},
    {"id": 8, "name": "vwx", "company_market": "tech"},
    {"id": 9, "name": "yz", "company_market": "healthcare"},
    {"id": 10, "name": "abc123", "company_market": "Finance"},
    # {"id": 11, "name": "yz", "company_market": "real estate"},
    {"id": 11, "name": "xz", "company_market": "cleaning"}
]

@app.get('/')
async def index() -> dict[str,str]:
    ## Also we are mention the return type of the api request
    ## Which helps in the data validation for response
    return {
        "hello" : "Universe"
    }
    ## If the return type varies from the mentioned return type on the function , it will raise an exception


@app.get('/companies',response_description="Companies fetched successfully")
async def bands() -> list[Company]:
    return [
        Company(**c) for c in companies
    ]

@app.get("/companies/{company_id}")
async def get_Company_details(company_id:int)->list[Company]:
    ## The purposes of the next is to retrive the first match
    ## We can also retain this with comprehsion, but the next() is more efficient
    ## also Hide all the iteration working behind
    details = next((Company(**c) for c in companies if c["id"] == company_id),None)
    if details:
        return [
            details
        ]
    raise HTTPException(status_code=404,detail="No company found")


## Understanding the path parameter
@app.get('/companies/market/{market}')
async def get_Market_based_company(market:generalizeMarkets)->list[Company]:
    return [
        Company(**c) for c in companies if c["company_market"].lower() == market.value
    ]
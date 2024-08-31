from fastapi import FastAPI

app = FastAPI()

## This is an simple endpoints on idea that
## how the fastapi is working

data = [
    {"id": 1, "name": "abc", "company_market": "cleaning"},
    {"id": 2, "name": "def", "company_market": "tech"},
    {"id": 3, "name": "ghi", "company_market": "finance"},
    {"id": 4, "name": "jkl", "company_market": "healthcare"},
    {"id": 5, "name": "mno", "company_market": "energy"},
    {"id": 6, "name": "pqr", "company_market": "retail"},
    {"id": 7, "name": "stu", "company_market": "manufacturing"},
    {"id": 8, "name": "vwx", "company_market": "transportation"},
    {"id": 9, "name": "yz", "company_market": "real estate"},
    {"id": 10, "name": "abc123", "company_market": "food service"}
]

@app.get('/')
async def index() -> dict[str,str]: ## Also we are mention the return type of the api request
                                    ## Which helps in the data validation for response
    return {
        "hello" : "Universe"
    } ## If the return type varies from the mentioned return type on the function , it will raise an exception


@app.get('/bands')
async def bands() -> list[dict]:
    return data


@app.get('/aboutMe')
async def aboutme() -> str:
    return (
        "I'm currently learning Fastapi"
    )
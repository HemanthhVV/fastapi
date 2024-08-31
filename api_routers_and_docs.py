from fastapi import FastAPI

app = FastAPI()

## This is an simple endpoints on idea that
## how the fastapi is working with g
@app.get('/')
async def index() -> dict[str,str]: ## Also we are mention the return type of the api request
                                    ## Which helps in the data validation for response
    return {
        "hello" : "Universe"
    } ## If the return type varies from the mentioned return type on the function , it will raise an exception

@app.get('/aboutMe')
async def aboutme() -> str:
    return (
        "I'm currently learning Fastapi"
    )
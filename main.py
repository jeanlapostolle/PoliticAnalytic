from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Validate the API connexion"}

@app.get("/cities/")
def get_city(city: str | None = None, insee_code: str | None = None):
    if city is None and insee_code is None:
        return {"message": "Please provide a city or an insee code"}
    if city is not None:
        return {"city": city}
    return {"insee_code": insee_code}
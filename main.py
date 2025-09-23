from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

class City(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    insee_code: int
    dep_id: int | None = Field(foreign_key="department.id")


engine = create_engine("sqlite:///electionFR.db")


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Validate the API connexion"}

@app.get("/cities/")
def get_city(city: str | None = None, insee_code: str | None = None):
    if city is None and insee_code is None:
        return {"message": "Please provide a city or an insee code"}
    if city is not None:
        with Session(engine) as session:
            statement = select(City).where(City.name == city)
            city = session.exec(statement).first()
        return {"city": city}
    return {"insee_code": insee_code}

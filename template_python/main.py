import uvicorn
from faker import Faker
from fastapi import FastAPI


app = FastAPI()
fake = Faker("jp-JP")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"H": fake.name()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

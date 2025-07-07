
from fastapi import FastAPI, HTTPException
from app.weather import get_weather

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/weather")
def weather(city: str):
    try:
        data = get_weather(city)
        return {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "descricao": data["weather"][0]["description"],
            "umidade": data["main"]["humidity"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

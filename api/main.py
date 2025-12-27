from fastapi import FastAPI
from api.health import router as health_router
from core.health_gate import enforce_health_gate

app = FastAPI(title="HormigasAIS Node API")

# El Guardián: Si la salud no es nominal, la API no arranca
enforce_health_gate()

app.include_router(health_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "HormigasAIS Protocol Node - LBH-2025 Active"}

import json
import os
from fastapi import FastAPI

app = FastAPI(title="HormigasAIS Protocol Node")

@app.get("/")
def read_root():
    return {"status": "online", "node": "Maestro", "protocol": "LBH"}

@app.get("/protocolo")
def get_protocolo():
    # Buscamos el archivo de especificación en la carpeta core
    path = os.path.join("core", "protocolo_lbh.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
        return data
    return {"error": "Archivo de protocolo no encontrado"}

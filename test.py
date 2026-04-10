from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import yaml

app = FastAPI()

# Cargamos tu archivo swagger.yaml
with open("swagger.yaml", "r", encoding="utf-8") as f:
    custom_openapi = yaml.safe_load(f)

@app.get("/")
def mostrar_usuario():
    return {"Hola": "Mundo", "Te logeastes desde la misma red": "Que tengas lindos Sueños"}

@app.get("/docs", include_in_schema=False)
def get_swagger_ui():
    # FastAPI servirá automáticamente la interfaz en /docs
    return app.openapi()

# Sobrescribimos el esquema interno con tu YAML
app.openapi_schema = custom_openapi

if __name__ == "__main__":
    import uvicorn
    print("🚀 Interfaz lista en: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
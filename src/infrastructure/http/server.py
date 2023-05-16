from os import makedirs

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from uvicorn import run

from src.infrastructure.http.controllers.test import medicament_router

# Create the directory if it doesn't exist
makedirs("uploads", exist_ok=True)

# Create the FastAPI app instance
app = FastAPI(
    title="Dynaccurate Desafio - Backend - TEST",
    description="API para o desafio Dynaccurate 2",
    version="0.0.5",
)

# Allow all origins to make requests
origins = ["*"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# To serve static files to clients
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Utils to automagically create pagination for the API
add_pagination(app)


# Health check endpoint
@app.get("/")
def check_health():
    return {
        "Entre /docs ou /redoc para visualizar a documentação da API": "Desafio Dynaccurate"
    }


# The only router in the application - CRUD Medicaments and upload endpoints
app.include_router(medicament_router)


# Run the application with ASGI Server Uvicorn
if __name__ == "__main__":
    run(
        app="src.infrastructure.http.server:app",
        host="0.0.0.0",
        port=3333,
        reload=True,
        log_level="debug",
    )

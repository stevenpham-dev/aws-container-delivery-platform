import os
from fastapi import FastAPI

APP_NAME = os.getenv("APP_NAME", "platform-api")
APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
APP_ENV = os.getenv("APP_ENV", "local")

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Simple FastAPI service for AWS container delivery platform demos.",
)


@app.get("/")
def read_root():
    return {
        "message": "AWS Container Delivery Platform API is running",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "app_name": APP_NAME,
        "version": APP_VERSION,
    }


@app.get("/version")
def version():
    return {
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
    }
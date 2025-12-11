from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur mon API Jalon 2 🚀"}




from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict")
def predict(features: list):
    pred = model.predict([features])[0]
    return {"prediction": float(pred)}

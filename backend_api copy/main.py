from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import joblib
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Import our orchestrator
from health_score_engine.orchestrator import calculate_health_score

# --- Initialization & Configuration ---
app = FastAPI(title="NirogX Health API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load environment variables securely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    print("WARNING: GEMINI_API_KEY not found in .env. AI Chat will not work.")

# Load existing black-box ML model
try:
    rf_model = joblib.load("random_forest_model.pkl")
    feature_names = joblib.load("feature_names.pkl")
    print("Model and features loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")

# --- Schemas ---
class HealthDataInput(BaseModel):
    symptoms: List[str] = []
    heart_rate: Optional[int] = None
    blood_pressure_systolic: Optional[int] = None
    blood_pressure_diastolic: Optional[int] = None
    daily_steps: Optional[int] = None
    age: Optional[int] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    sleep_hours: Optional[float] = None

class ChatInput(BaseModel):
    message: str
    health_context: Optional[HealthDataInput] = None

# --- Endpoints ---
@app.get("/")
def read_root():
    return {"message": "NirogX API is running successfully!"}

@app.get("/symptoms")
def get_symptoms():
    return {"symptoms": feature_names}

@app.post("/predict")
def predict_disease(data: HealthDataInput):
    if not data.symptoms:
        raise HTTPException(status_code=400, detail="Please provide at least one symptom.")
    
    input_data = {feature: 0 for feature in feature_names}
    for symptom in data.symptoms:
        if symptom in input_data:
            input_data[symptom] = 1
            
    df = pd.DataFrame([input_data])
    try:
        prediction = rf_model.predict(df)[0]
        return {"prediction": prediction, "symptoms_analyzed": data.symptoms}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/health-score")
def get_health_score(data: HealthDataInput):
    ml_prediction = None
    if data.symptoms:
        input_data = {feature: 0 for feature in feature_names}
        for symptom in data.symptoms:
            if symptom in input_data:
                input_data[symptom] = 1
        df = pd.DataFrame([input_data])
        try:
            ml_prediction = rf_model.predict(df)[0]
        except Exception:
            pass 
            
    result = calculate_health_score(data.model_dump(), ml_prediction)
    return result

# NEW ENDPOINT: AI Chat API
@app.post("/chat")
def ai_chat(data: ChatInput):
    if not api_key:
        raise HTTPException(status_code=500, detail="AI API key is missing. Check backend configuration.")

    try:
        # Use active Gemini model
        model = genai.GenerativeModel('gemini-3.6-flash')
        
        # Inject the user's data into the system context invisibly
        prompt = "You are the NirogX AI Health Assistant. Answer the user's question concisely and empathetically. DO NOT provide medical diagnoses.\n\n"
        
        if data.health_context:
            prompt += "--- USER'S CURRENT HEALTH DATA (Use as invisible context) ---\n"
            if data.health_context.symptoms:
                prompt += f"Symptoms: {', '.join(data.health_context.symptoms)}\n"
            if data.health_context.heart_rate:
                prompt += f"Heart Rate: {data.health_context.heart_rate} bpm\n"
            if data.health_context.blood_pressure_systolic:
                prompt += f"Blood Pressure: {data.health_context.blood_pressure_systolic}/{data.health_context.blood_pressure_diastolic} mmHg\n"
            if data.health_context.daily_steps:
                prompt += f"Daily Steps: {data.health_context.daily_steps}\n"
            prompt += "-----------------------------------------------------------\n\n"
            
        prompt += f"User's Message: {data.message}\n"
        
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            raise Exception("Empty response from AI Model")
            
        return {"response": response.text}
        
    except Exception as e:
        # FIX: Explicitly print the error in the terminal so we can see why it fails
        print(f"DEBUG Chat Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI Chat error: {str(e)}")
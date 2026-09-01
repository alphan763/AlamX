import os

os.makedirs("health_score_engine", exist_ok=True)

files = {
    "__init__.py": "",
    
    "heart_rate.py": """def score_heart_rate(hr: int, age: int = None) -> dict:
    if hr is None or hr <= 0:
        return {"available": False}
    if 60 <= hr <= 100:
        return {"score": 15, "maxScore": 15, "available": True, "status": "good", "note": "Resting heart rate is within the expected normal range."}
    elif 50 <= hr < 60 or 100 < hr <= 109:
        return {"score": 7, "maxScore": 15, "available": True, "status": "attention", "note": "Resting heart rate is slightly outside standard ranges."}
    else:
        return {"score": 0, "maxScore": 15, "available": True, "status": "attention", "note": "Resting heart rate reading indicates attention may be needed."}
""",

    "blood_pressure.py": """def score_blood_pressure(systolic: int, diastolic: int) -> dict:
    if not systolic or not diastolic or systolic <= 0 or diastolic <= 0:
        return {"available": False}
    if systolic < 120 and diastolic < 80:
        return {"score": 25, "maxScore": 25, "available": True, "status": "good", "note": "Blood pressure is in the normal range (AHA guidelines)."}
    elif 120 <= systolic <= 129 and diastolic < 80:
        return {"score": 15, "maxScore": 25, "available": True, "status": "attention", "note": "Blood pressure is elevated."}
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        return {"score": 5, "maxScore": 25, "available": True, "status": "attention", "note": "Blood pressure corresponds to Stage 1 levels."}
    else:
        return {"score": 0, "maxScore": 25, "available": True, "status": "attention", "note": "Blood pressure corresponds to Stage 2 or higher levels."}
""",

    "activity.py": """def score_activity(steps: int) -> dict:
    if steps is None or steps < 0:
        return {"available": False}
    if steps >= 8000:
        return {"score": 20, "maxScore": 20, "available": True, "status": "good", "note": "Excellent daily activity level."}
    elif steps >= 5000:
        return {"score": 10, "maxScore": 20, "available": True, "status": "attention", "note": "Moderate daily activity; consider increasing movement."}
    else:
        return {"score": 0, "maxScore": 20, "available": True, "status": "attention", "note": "Low daily activity level."}
""",

    "symptoms_ml.py": """def score_symptoms_ml(symptoms_list: list, ml_prediction: str) -> dict:
    if not symptoms_list or len(symptoms_list) == 0:
        return {"score": 30, "maxScore": 30, "available": True, "status": "good", "note": "No symptoms reported."}
    if not ml_prediction:
        return {"available": False}
    if len(symptoms_list) <= 2:
        return {"score": 15, "maxScore": 30, "available": True, "status": "attention", "note": f"Minor symptoms reported. Application-derived indicator: {ml_prediction}."}
    return {"score": 0, "maxScore": 30, "available": True, "status": "attention", "note": f"Multiple symptoms reported. Application-derived indicator: {ml_prediction}."}
""",

    "supporting_factors.py": """def score_supporting_factors(height_cm: float, weight_kg: float, sleep_hours: float) -> dict:
    score, max_score, available, notes = 0, 10, False, []
    if height_cm and weight_kg and height_cm > 0 and weight_kg > 0:
        available = True
        bmi = weight_kg / ((height_cm / 100) ** 2)
        if 18.5 <= bmi <= 24.9:
            score += 5
            notes.append("BMI is within the standard healthy range.")
        else:
            notes.append("BMI is outside the standard healthy range.")
    if sleep_hours and sleep_hours > 0:
        available = True
        if 7 <= sleep_hours <= 9:
            score += 5
            notes.append("Sleep duration is optimal.")
        else:
            notes.append("Sleep duration is outside optimal guidelines.")
            
    if not available:
        return {"available": False}
    return {"score": score, "maxScore": max_score, "available": True, "status": "good" if score >= 7 else "attention", "note": " ".join(notes)}
""",

    "weighting.py": """def normalize_scores(components: dict) -> tuple:
    total_earned, total_possible = 0, 0
    for comp in components.values():
        if comp.get("available", False):
            total_earned += comp.get("score", 0)
            total_possible += comp.get("maxScore", 0)
    if total_possible == 0:
        return 0, 0, 0
    return int(round((total_earned / total_possible) * 100)), total_earned, total_possible
""",

    "orchestrator.py": """from .heart_rate import score_heart_rate
from .blood_pressure import score_blood_pressure
from .activity import score_activity
from .symptoms_ml import score_symptoms_ml
from .supporting_factors import score_supporting_factors
from .weighting import normalize_scores

def calculate_health_score(data: dict, ml_prediction: str = None) -> dict:
    comps = {
        "heartRate": score_heart_rate(data.get("heart_rate"), data.get("age")),
        "bloodPressure": score_blood_pressure(data.get("blood_pressure_systolic"), data.get("blood_pressure_diastolic")),
        "activity": score_activity(data.get("daily_steps")),
        "symptomsMl": score_symptoms_ml(data.get("symptoms", []), ml_prediction),
        "supportingFactors": score_supporting_factors(data.get("height_cm"), data.get("weight_kg"), data.get("sleep_hours"))
    }
    
    active_comps = {k: v for k, v in comps.items() if v.get("available", False)}
    overall_score, _, _ = normalize_scores(active_comps)
    
    positive = [v["note"] for v in active_comps.values() if v["status"] == "good"]
    attention = [v["note"] for v in active_comps.values() if v["status"] in ["attention", "concern"]]
            
    return {
        "overallScore": overall_score if active_comps else None,
        "indicatorsUsed": len(active_comps),
        "indicatorsTotal": 5,
        "components": active_comps,
        "positiveIndicators": positive,
        "attentionIndicators": attention,
        "disclaimer": "This is an application-derived wellness indicator, not a medical diagnosis. It does not replace professional clinical assessment."
    }
"""
}

for filename, content in files.items():
    with open(f"health_score_engine/{filename}", "w") as f:
        f.write(content)

print("Health Score Engine modules generated successfully!")
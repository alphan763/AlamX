from .heart_rate import score_heart_rate
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

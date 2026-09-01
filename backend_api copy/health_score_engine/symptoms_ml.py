def score_symptoms_ml(symptoms_list: list, ml_prediction: str) -> dict:
    if not symptoms_list or len(symptoms_list) == 0:
        return {"score": 30, "maxScore": 30, "available": True, "status": "good", "note": "No symptoms reported."}
    if not ml_prediction:
        return {"available": False}
    if len(symptoms_list) <= 2:
        return {"score": 15, "maxScore": 30, "available": True, "status": "attention", "note": f"Minor symptoms reported. Application-derived indicator: {ml_prediction}."}
    return {"score": 0, "maxScore": 30, "available": True, "status": "attention", "note": f"Multiple symptoms reported. Application-derived indicator: {ml_prediction}."}

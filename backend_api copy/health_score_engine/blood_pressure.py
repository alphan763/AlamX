def score_blood_pressure(systolic: int, diastolic: int) -> dict:
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

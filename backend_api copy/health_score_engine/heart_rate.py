def score_heart_rate(hr: int, age: int = None) -> dict:
    if hr is None or hr <= 0:
        return {"available": False}
    if 60 <= hr <= 100:
        return {"score": 15, "maxScore": 15, "available": True, "status": "good", "note": "Resting heart rate is within the expected normal range."}
    elif 50 <= hr < 60 or 100 < hr <= 109:
        return {"score": 7, "maxScore": 15, "available": True, "status": "attention", "note": "Resting heart rate is slightly outside standard ranges."}
    else:
        return {"score": 0, "maxScore": 15, "available": True, "status": "attention", "note": "Resting heart rate reading indicates attention may be needed."}

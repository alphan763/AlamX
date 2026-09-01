def score_activity(steps: int) -> dict:
    if steps is None or steps < 0:
        return {"available": False}
    if steps >= 8000:
        return {"score": 20, "maxScore": 20, "available": True, "status": "good", "note": "Excellent daily activity level."}
    elif steps >= 5000:
        return {"score": 10, "maxScore": 20, "available": True, "status": "attention", "note": "Moderate daily activity; consider increasing movement."}
    else:
        return {"score": 0, "maxScore": 20, "available": True, "status": "attention", "note": "Low daily activity level."}

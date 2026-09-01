def score_supporting_factors(height_cm: float, weight_kg: float, sleep_hours: float) -> dict:
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

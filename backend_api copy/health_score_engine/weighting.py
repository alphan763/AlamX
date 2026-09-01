def normalize_scores(components: dict) -> tuple:
    total_earned, total_possible = 0, 0
    for comp in components.values():
        if comp.get("available", False):
            total_earned += comp.get("score", 0)
            total_possible += comp.get("maxScore", 0)
    if total_possible == 0:
        return 0, 0, 0
    return int(round((total_earned / total_possible) * 100)), total_earned, total_possible

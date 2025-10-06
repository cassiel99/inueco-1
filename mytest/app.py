from typing import List, Optional, Dict, Any

def analyze_temperature(temperatures: List[int]) -> Optional[Dict[str, Any]]:

    if not temperatures or len(temperatures) != 7:
        return None

    avg = round(sum(temperatures) / 7, 1)
    return {
        "average": avg,
        "max": max(temperatures),
        "min": min(temperatures),
        "hot_days": sum(1 for t in temperatures if t > 25),
        "cold_days": sum(1 for t in temperatures if t < 10),
    }

temperatures = [22, 28, 15, 8, 30, 18, 25]
result = analyze_temperature(temperatures)
print(result)

temperatures = [15, 16, 17]
result = analyze_temperature(temperatures)
print(result)

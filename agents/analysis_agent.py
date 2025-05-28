from typing import Dict, List

def analyze_market(market_data: Dict[str, dict], earnings_docs: List[str]) -> Dict:
    analysis = {}
    total_allocation = 0
    beat_count = 0
    miss_count = 0

    for symbol, data in market_data.items():
        if "percent_change" in data:
            allocation = round(abs(data["percent_change"]), 2)
            analysis[symbol] = {
                "percent_change": data["percent_change"],
                "allocation": allocation
            }
            total_allocation += allocation

    for doc in earnings_docs:
        if "beat" in doc.lower(): beat_count += 1
        elif "miss" in doc.lower(): miss_count += 1

    sentiment = "neutral"
    if beat_count > miss_count: sentiment = "positive"
    elif miss_count > beat_count: sentiment = "cautionary"

    return {
        "symbol_analysis": analysis,
        "total_asia_tech_allocation": round(total_allocation, 2),
        "earnings_summary": {
            "beats": beat_count,
            "misses": miss_count,
            "sentiment": sentiment
        }
    }
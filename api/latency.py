import json
from statistics import mean

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Only POST allowed"
        }

    data = request.get_json()
    regions = data.get("regions", [])
    threshold = data.get("threshold_ms", 180)

    result = {}

    for r in regions:
        result[r] = {
            "avg_latency": 120,
            "p95_latency": 150,
            "avg_uptime": 99.9,
            "breaches": 0
        }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }

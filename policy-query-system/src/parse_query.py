import json

def parse_query(raw: str):
    """Hackathon placeholder parser."""
    return {
        "age": 46,
        "gender": "male",
        "procedure": "knee surgery",
        "location": "pune",
        "policy_age_days": 90
    }

if __name__ == "__main__":
    print(json.dumps(parse_query(""), indent=2))
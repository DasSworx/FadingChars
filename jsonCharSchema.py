from jsonschema import validate, ValidationError


jsonCharSchema = {
    "type": "object",
    "properties": {
        "header": {
            "type": "object",
            "properties": {
                "Name": {"type": "string"},
                "Rank": {"type": "string"},
                "Species": {"type": "string"}
            },
            "required": ["Name", "Rank", "Species"],
            "additionalProperties": False
        },
        "overview": {
            "type": "object",
            "properties": {
                "Class": {"type": "string"},
                "Faction": {"type": "string"},
                "Level": {"type": "integer"}
            },
            "required": ["Class", "Faction", "Level"],
            "additionalProperties": False
        },
        "skills": {
            "type": "object",
            "properties": {
                "Academia": {"type": "integer"},
                "Alchemy": {"type": "integer"},
                "Animalia": {"type": "integer"},
                "Arts": {"type": "integer"},
                "Charm": {"type": "integer"},
                "Crafts": {"type": "integer"},
                "Disguise": {"type": "integer"},
                "Drive": {"type": "integer"},
                "Empathy": {"type": "integer"},
                "Fight": {"type": "integer"},
                "Focus": {"type": "integer"},
                "Impress": {"type": "integer"},
                "Interface": {"type": "integer"},
                "Intrusion": {"type": "integer"},
                "Knavery": {"type": "integer"},
                "Melee": {"type": "integer"},
                "Observe": {"type": "integer"},
                "Perform": {"type": "integer"},
                "Pilot": {"type": "integer"},
                "Remedy": {"type": "integer"},
                "Shoot": {"type": "integer"},
                "Sleight of Hand": {"type": "integer"},
                "Sneak": {"type": "integer"},
                "Survival": {"type": "integer"},
                "Tech Redemption": {"type": "integer"},
                "Vigor": {"type": "integer"}
            },
            "required": ["Academia", "Alchemy", "Animalia", "Arts", "Charm", "Crafts", "Disguise", "Drive", "Empathy", "Fight", "Focus", "Impress", "Interface", "Intrusion", "Knavery", "Melee", "Observe", "Perform", "Pilot", "Remedy", "Shoot", "Sleight of Hand", "Sneak", "Survival", "Tech Redemption", "Vigor"],
            "additionalProperties": False
        },
        "occult": {
            "type": "object",
            "properties": {
                "Psi": {"type": "integer"},
                "Urge": {"type": "integer"},
                "Theurgy": {"type": "integer"},
                "Hubris": {"type": "integer"}
            },
            "required": ["Psi", "Urge", "Theurgy", "Hubris"],
            "additionalProperties": False
        }
    },
    "required": ["header", "overview", "skills", "occult"],
    "additionalProperties": False
}
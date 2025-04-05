from jsonschema import validate, ValidationError


jsonCharSchema = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
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
        },
        "characteristics": {
            "type": "object",
            "properties": {
                "Body": {
                    "type": "object",
                    "properties": {
                        "Strength": {"type": "integer"},
                        "Dexterity": {"type": "integer"},
                        "Endurance": {"type": "integer"},
                    },
                    "requirements": ["Strength", "Dexterity", "Endurance"],
                    "additionalProperties": False
                },
                "Mind": {
                    "type": "object",
                    "properties": {
                        "Wits": {"type": "integer"},
                        "Perception": {"type": "integer"},
                        "Will": {"type": "integer"},
                    },
                    "requirements": ["Wits", "Perception", "Will"],
                    "additionalProperties": False
                },
                "Spirit": {
                    "type": "object",
                    "properties": {
                        "Presence": {"type": "integer"},
                        "Intuition": {"type": "integer"},
                        "Faith": {"type": "integer"},
                    },
                    "requirements": ["Presence", "Intuition", "Faith"],
                    "additionalProperties": False
                }
            },
            "required": ["Body", "Mind", "Spirit"],
            "additionalProperties": False
        },
        "durability": {
            "type": "object",
            "properties": {
                "Resistances": {
                    "type": "object",
                    "properties": {
                        "Body": {"type": "integer"},
                        "Mind": {"type": "integer"},
                        "Spirit": {"type": "integer"}
                    },
                    "required": ["Body", "Mind", "Spirit"],
                    "additionalProperties": False
                },
                "Armor": {
                    "type": "object",
                    "properties": {
                        "Model": {"type": "string"},
                        "Value": {"type": "integer"}
                    },
                    "required": ["Model","Value"]
                },
                "E-Shield": {
                    "type": "object",
                    "properties": {
                        "Model": {"type": "string"},
                        "Lower_Threshold": {"type": "integer"},
                        "Upper_Threshold": {"type": "integer"},
                        "Hits": {"type": "integer"}
                    },
                    "required": ["Model", "Lower_Threshold", "Upper_Threshold", "Hits"],
                    "additionalProperties": False
                },
                "Vitality": {"type": "integer"},
                "Revivals": {"type": "integer"}
            },
            "required": ["Resistances", "Armor", "E-Shield", "Vitality", "Revivals"],
            "additionalProperties": False
        },
        "actions": {
            "type": "array",
            "action": {
                "type": "object",
                "properties": {
                    "Name": {"type": "string"},
                    "Goal": {"type": "integer"},
                    "Impact": {"type": "string"}
                },
                "required": ["Name", "Goal"],
                "additionalProperties": False
            }
        },
        "vp bank": {
            "type": "object",
            "properties": {
                "Capacity": {"type": "integer"}
            },
        "required": ["Capacity"],
        "additionalProperties": False
        },
        "surge": {
            "type": "object",
            "properties": {
                "Rating": {"type": "integer"},
                "Number": {"type": "integer"}
            },
        "required": ["Rating", "Number"],
        "additionalProperties": False
        },
        "perks": {
            "type": "array",
            "item": {"type": "string"}
        },
        "capabilities": {
            "type": "array",
            "item": {"type": "string"}
        },
        "birthrights": {
            "type": "array",
            "item": {"type": "string"}
        }
    },
    "required": ["header", "overview", "skills", "occult", "characteristics",
                 "durability", "vp bank", "surge", "perks"],
    "additionalProperties": False
}
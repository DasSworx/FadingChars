from jsonschema import validate, ValidationError


jsonCharSchema = {
    "type" : "object",
    "properties" :{
    "name" : {"type": "string"},
    "age" : {"type" : "integer"}
    },
    "required": ["name", "age"],
    "additionalProperties" : False
}
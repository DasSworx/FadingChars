from jsonschema import validate, ValidationError
import jsonCharSchema as jSchema
import json

import jsonCharSchema

with open("C:/Users/Jesus/Documents/Rollenspiele/Fading Suns/Characters/TestChar.json", "r") as file:
    testChar = json.load(file)

try:
    validate(instance=testChar, schema=jSchema.jsonCharSchema)
    print("JSON is valid")
except ValidationError as e:
    print("JSON validation error:", e.message)
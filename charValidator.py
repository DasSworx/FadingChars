from jsonschema import validate, ValidationError
import jsonCharSchema as jSchema
import json

import jsonCharSchema

def jsonCharIsValid(pathToChar) -> bool:

    try:
        with open(pathToChar, "r") as file:
            testChar = json.load(file)
    except FileNotFoundError as e:
        print("File could not be opened:", e.filename)
        return False

    try:
        validate(instance=testChar, schema=jSchema.jsonCharSchema)
        print("JSON is valid")
        return True
    except ValidationError as e:
        print("JSON validation error:", e.message)
        return False

jsonCharIsValid("./src/BlankChar.json")
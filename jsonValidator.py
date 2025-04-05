from jsonschema import validate, ValidationError
import json
import os

def jsonIsValid(pathToJson, jsonSchema) -> bool:

    if not os.path.exists(pathToJson):
        print("The pathToJson does not exist")
        return False
    if not (os.path.exists(jsonSchema)):
        print("The jsonSchema does not exist")
        return False

    try:
        with open(pathToJson, "r") as file:
            testChar = json.load(file)
    except json.JSONDecodeError as e:
        print("File could not be opened:", e)
        return False

    try:
        with open(jsonSchema, "r") as schema:
            jsonCharSchema = json.load(schema)
    except json.JSONDecodeError as e:
        print("decode error: ", e)


    try:
        validate(instance = testChar, schema = jsonCharSchema)
        print("JSON is valid")
        return True
    except ValidationError as e:
        print("JSON validation error:", e.message)
        return False
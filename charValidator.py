from jsonschema import validate, ValidationError
import json
import os

def jsonCharIsValid(pathToChar, charSchema) -> bool:

    if not os.path.exists(pathToChar):
        print("The pathToChar does not exist")
        return False
    if not (os.path.exists(charSchema)):
        print("The charSchema does not exist")
        return False

    try:
        with open(pathToChar, "r") as file:
            testChar = json.load(file)
    except json.JSONDecodeError as e:
        print("File could not be opened:", e)
        return False

    try:
        with open(charSchema, "r") as schema:
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

jsonCharIsValid("./src/BlankChar.json", "./src/jsonCharSchema.json")
import json
import os
from jsonschema import validate, ValidationError

class FadingChar:
    def __init__(self, pathToCharFile: str):
        self.pathToCharFile = pathToCharFile
        with open(pathToCharFile, "r") as charFile:
            self.char = json.load(charFile)

###### HELPER FUNCTIONS #####
    def charIsValid(self, charSchema: str) -> bool:
        if not (os.path.exists(charSchema)):
            print("The charSchema does not exist")
            return False
        try:
            with open(charSchema, "r") as schema:
                jsonCharSchema = json.load(schema)
        except json.JSONDecodeError as e:
            print("decode error: ", e)
        try:
            validate(instance=self.char, schema=jsonCharSchema)
            print("JSON is valid")
            return True
        except ValidationError as e:
            print("JSON validation error:", e.message)
            return False

    def getProperty(self, nameOfProperty: str) -> str:
        splitPath = nameOfProperty.split(".")
        copyOfSelfChar = self.char
        for partOfPath in splitPath:
            copyOfSelfChar = copyOfSelfChar[partOfPath]
            return copyOfSelfChar[splitPath[-1]]

    def setProperty(self, nameOfProperty: str, valueOfProperty):
        splitPath = nameOfProperty.split(".")
        copyOfSelfChar = self.char
        for partOfPath in splitPath[:-1]:
            copyOfSelfChar = copyOfSelfChar[partOfPath]
            copyOfSelfChar[splitPath[-1]] = valueOfProperty
        if self.charIsValid("./src/jsonCharSchema.json"):
            print(f"Property {nameOfProperty} was set to {valueOfProperty}")

    def saveChanges(self):
        with open(self.pathToCharFile, "w") as file:
            json.dump(self.char, file, indent=4)

import editCharJson, jsonValidator
from editCharJson import FadingChar

newChar = FadingChar("./src/BlankChar.json")
newChar.setProperty("header.Name", "Steve")
print(newChar.char)
print(newChar.getProperty("header.Name"))
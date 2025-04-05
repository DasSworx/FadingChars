import editCharJson, jsonValidator
from editCharJson import FadingChar

newChar = FadingChar("./src/BlankChar.json")
newChar.setProperty("header.Name", "")
print(newChar.char)
newChar.saveChanges()
import os

filename = "Completion_Statement.html"
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    "â‚¬": "€",
    "Â£": "£",
    "â€“": "–",
    "â€”": "—",
    "Ã©": "é",
    "Ã±": "ñ",
    "Ã“": "Ó",
    "â€™": "’"
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

print("Encoding successfully fixed!")

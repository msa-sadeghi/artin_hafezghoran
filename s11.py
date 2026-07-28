import json

students = [{"name": "armin", "score": 92}, {"name": "maryam", "score": 91}]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)


with open("students.json", "r") as f:
    loaded = json.load(f)

for s in loaded:
    print(s["name"], s["score"])

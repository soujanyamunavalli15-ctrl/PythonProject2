import json

# Open and load JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Print formatted output
print("===== STUDENT DETAILS =====")
print("Name   :", data["name"])
print("Age    :", data["age"])
print("Course :", data["course"])
print("College:", data["college"])

print("Skills :")
for skill in data["skills"]:
    print("-", skill)
# Считать JSON с ответами
import json
import pickle

with open('quiz_data.json', "rb") as json_file:
    data = pickle.load(json_file)

score = 0
if data["q1"] == "8":
    score += 1
if data["q2"] == "10":
    score += 1
if data["q3"] == "13":
    score += 1

print(f"{score} {data['now']}")
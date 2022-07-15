import json
import pickle
from datetime import datetime

if __name__ == "__main__":
    q1 = input("5 + 3 = ")
    q2 = input("5 + 5 = ")
    q3 = input("5 + 8 = ")

    data = {"now": str(datetime.now()), "q1": q1, "q2": q2, "q3": q3}

    with open('quiz_data.json', "wb") as json_file:
        pickle.dump(data, json_file)


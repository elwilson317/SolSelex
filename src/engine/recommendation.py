import json

ENGINEERING_DATA = "assets/engineering_data.json"


def load_engineering_data():
    with open(ENGINEERING_DATA, "r") as file:
        return json.load(file)


LAND_DATA = load_engineering_data()


def get_recommendation(predicted_class):
    return LAND_DATA[predicted_class]
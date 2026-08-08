LAND_SCORES = {

    "AnnualCrop": {
        "score": 70,
        "recommendation": "Moderately Suitable",
        "reason": "Flat land but may compete with agriculture."
    },

    "Forest": {
        "score": 15,
        "recommendation": "Unsuitable",
        "reason": "Dense vegetation causes shading and environmental concerns."
    },

    "HerbaceousVegetation": {
        "score": 95,
        "recommendation": "Highly Suitable",
        "reason": "Open vegetation with minimal shading."
    },

    "Highway": {
        "score": 20,
        "recommendation": "Unsuitable",
        "reason": "Transportation corridor."
    },

    "Industrial": {
        "score": 60,
        "recommendation": "Conditionally Suitable",
        "reason": "Possible rooftop or brownfield installation."
    },

    "Pasture": {
        "score": 92,
        "recommendation": "Highly Suitable",
        "reason": "Large open land suitable for solar panels."
    },

    "PermanentCrop": {
        "score": 45,
        "recommendation": "Low Suitability",
        "reason": "Avoid disturbing long-term agricultural land."
    },

    "Residential": {
        "score": 25,
        "recommendation": "Unsuitable",
        "reason": "Dense residential development."
    },

    "River": {
        "score": 0,
        "recommendation": "Unsuitable",
        "reason": "Water body."
    },

    "SeaLake": {
        "score": 0,
        "recommendation": "Unsuitable",
        "reason": "Water body."
    }
}


def get_recommendation(predicted_class):

    return LAND_SCORES[predicted_class]
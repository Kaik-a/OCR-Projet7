from typing import Dict, List

import requests

from . import GMAPS


def get_location(questions: List) -> List[Dict]:
    """
    Get the location from a question.

    :param List questions: questions to search for.

    :rtype List[Dict]
    """
    results = [
        requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json",
            {
                "address": address,
                # "components": "country:FR",
                "key": GMAPS,
            },
        ).json()
        for address in questions
    ]

    locations = [
        {
            "coordonates": result["results"][0]["geometry"]["location"],
            "address": result["results"][0]["formatted_address"],
        }
        for result in results
        if result["results"]
    ]

    for location in locations:
        location["coordonates"]["lat"] = float(location["coordonates"]["lat"])
        location["coordonates"]["lng"] = float(location["coordonates"]["lng"])

    return locations

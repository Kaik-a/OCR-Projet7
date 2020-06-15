import requests
from typing import Dict, List


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
                'address': address,
                'key': 'AIzaSyAI6WPMSEM0YvN81wqDaZsnbNmKNldwe_4'
            }
        ).json()
        for address in questions
    ]

    coordonates = [
        result['results'][0]['geometry']['location'] for result in results
        if result
    ]

    for coordonate in coordonates:
        coordonate['lat'] = float(coordonate['lat'])
        coordonate['lng'] = float(coordonate['lng'])

    return coordonates


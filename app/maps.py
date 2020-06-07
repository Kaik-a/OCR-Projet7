from typing import Dict, List

import googlemaps


def get_location(questions: List) -> List[Dict]:
    """
    Get the location from a question.

    :param List questions: questions to search for.

    :rtype List[Dict]
    """
    gmaps = googlemaps.Client(key='AIzaSyAI6WPMSEM0YvN81wqDaZsnbNmKNldwe_4')

    results: List = [gmaps.geocode(question) for question in questions]
    coordonates = [
        result[0]['geometry']['location'] for result in results if result
    ]

    for coordonate in coordonates:
        coordonate['lat'] = float(coordonate['lat'])
        coordonate['lng'] = float(coordonate['lng'])

    return coordonates


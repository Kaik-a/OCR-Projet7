from typing import Dict
import googlemaps


def get_location(question: str) -> Dict:
    """
    Get the location from a question

    :param str question: question to search for

    :rtype Dict
    """
    gmaps = googlemaps.Client(key='AIzaSyAI6WPMSEM0YvN81wqDaZsnbNmKNldwe_4')

    result = gmaps.geocode('auchan nogent sur oise')

    coordonates = result[0]['geometry']['location']

    return coordonates


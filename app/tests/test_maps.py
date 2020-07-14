import unittest.mock as mock

import requests
from app import maps

from . import EIFFEL_TOWER_LOC


def test_get_location():
    """
    Function must parse request return value to store the
    coordonates and the adress of the desired location.
    """
    requests.get.json = mock.Mock(
        return_value=[
            {
                "results": [
                    {
                        "formated_address": "Champ de Mars, 5 Avenue Anatole France"
                        ", 75007 Paris, France",
                        "geometry": {"location": EIFFEL_TOWER_LOC},
                    }
                ]
            }
        ]
    )

    eiffel_tower = maps.get_location(["tour eiffel"])[0]

    assert eiffel_tower["coordonates"] == EIFFEL_TOWER_LOC

    assert (
        eiffel_tower["address"]
        == "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
    )

    assert maps.get_location(["abcdefghzi"]) == []

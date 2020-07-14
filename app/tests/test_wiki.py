"""tests Media Wiki interface"""
import unittest.mock as mock

import requests
from app import wiki

from ..wiki import INTRODUCTION
from . import EIFFEL_TOWER_ABSTRACT, EIFFEL_TOWER_LOC, OCR_QUESTION


def test_get_info_on_loc():
    """
    Function must return location of given place.
    """
    requests.get.json = mock.Mock(
        return_value={"query": {"geosearch": {"title": "tour eiffel"}}}
    )

    patch = mock.patch(
        "app.wiki.get_summary",
        new=mock.Mock(
            return_value="La tour Eiffel  est une tour de fer puddlé de "
            "324\xa0mètres de hauteur (avec antennes) située à "
            "Paris, à ...breuses expériences scientifiques".lower()
        ),
    )

    patch.start()

    assert "tour eiffel" in wiki.get_info_on_loc([EIFFEL_TOWER_LOC], ["tour eiffel"])
    patch.stop()


def test_get_summary():
    """
    Function must retrieve summary of place on a given location.
    """
    patch = mock.patch(
        "requests.get.json",
        new=mock.Mock(
            return_value={
                "query": {
                    "pages": {
                        1359783: {
                            "extract": 'p class="mw-empty-elt">\n\n</p>\n\n\n\n<p>La '
                            "<b>tour Eiffel</b>  est une tour de fer "
                            "puddlé de 324\xa0mètres de hauteur (avec "
                            "antennes) située à Paris, à l’extrémité "
                            "nord-ouest du parc du Champ-de-Mars en "
                            "bordure de la Seine dans le <abbr "
                            'class="abbr" '
                            'title="Septième">7<sup>e</sup></abbr'
                            ">\xa0arrondissement. Son adresse officielle "
                            "est 5, avenue Anatole-France. Construit par "
                            "Gustave Eiffel et ses collaborateurs pour "
                            "l’Exposition universelle de Paris de 1889, "
                            "et initialement nommée «\xa0tour de "
                            "300\xa0mètres\xa0», ce monument est devenu le"
                            " symbole de la capitale française et un site "
                            "touristique de premier plan\xa0: il s’agit du"
                            " troisième site culturel français payant le "
                            "plus visité en 2015, avec 5,9\xa0millions de "
                            "visiteurs en 2016 et du monument culturel "
                            'payant <span title="Ce passage semble en '
                            "contradiction avec un autre passage marqué ("
                            'demandé le 6 juin 2020).">le plus visité au '
                            'monde</span><sup class="need_ref_tag" '
                            'style="padding-left:2px;">['
                            'Contradiction]</sup><sup class="reference '
                            'cite_virgule">,</sup> en 2011. Depuis son '
                            "ouverture au public, elle a accueilli plus de"
                            " 300 millions de visiteurs.\n</p><p>D’une "
                            "hauteur de 312\xa0mètres à l’origine, la tour"
                            " Eiffel est restée le monument le plus élevé "
                            "du monde pendant quarante ans. Le second "
                            "niveau du troisième étage, appelé parfois "
                            "quatrième étage, situé à 279,11\xa0mètres, "
                            "est la plus haute plateforme d'observation "
                            "accessible au public de l'Union européenne "
                            "et la deuxième plus haute d'Europe, derrière "
                            "la tour Ostankino à Moscou culminant à "
                            "337\xa0mètres. La hauteur de la tour a été "
                            "plusieurs fois augmentée par l’installation "
                            "de nombreuses antennes. Utilisée dans le "
                            "passé pour de nombreuses expériences "
                            "scientifiques, elle sert aujourd’hui "
                            "d’émetteur de programmes radiophoniques et "
                            "télévisés.\n</p>\n\n\n<h2> "
                        }
                    }
                }
            }
        ),
    )

    patch.start()

    assert (
        wiki.get_summary({"title": "Tour Eiffel", "pageid": 1359783})
        == EIFFEL_TOWER_ABSTRACT
    )

    patch.stop()


def test_endow():
    """
    Function must add decorator to given sentence.
    """
    test = wiki.endow(OCR_QUESTION)

    assert any(element in test for element in INTRODUCTION)

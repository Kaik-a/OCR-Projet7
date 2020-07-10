"""tests on parser module"""
from application import parser

from . import MENTOR_1, MENTOR_2, OCR_QUESTION


def test_parse():
    assert parser.parse(OCR_QUESTION) == [
        "est-ce que tu connais l'adresse d'openclassrooms ?"
    ]

    assert parser.parse(MENTOR_1) == [
        "comment s'est passé ta soirée avec grandma hier soir?",
        "où se trouve le musée d'art et d'histoire de fribourg," " s'il te plaît?",
    ]

    assert parser.parse(MENTOR_2) == [
        "bonsoir grandpy, j'espère que tu as passé une belle semaine. est-ce "
        "que tu pourrais m'indiquer l'adresse de la tour eiffel? merci d'avance"
        " et salutations à mamie."
    ]


def test_unclutter():
    assert parser.unclutter([OCR_QUESTION]) == ["Est- l' d'OpenClassrooms ?"]

    assert parser.unclutter([MENTOR_1]) == [
        "Salut grandpy! Comment s' passé soirée Grandma hier soir? "
        "Au fait, j' pense, pourrais- m'indiquer où trouve musée d'art "
        "d'histoire Fribourg, s' plaît?"
    ]

    assert parser.unclutter([MENTOR_2]) == [
        "Bonsoir Grandpy, j'espère passé belle semaine. Est- m'indiquer "
        "l' tour eiffel? Merci d'avance salutations à Mamie."
    ]


def test_punctuation_and_accent():
    assert parser.punctuation_and_accent([OCR_QUESTION]) == [
        "Est ce que tu connais l adresse d OpenClassrooms "
    ]

    assert parser.punctuation_and_accent([MENTOR_1]) == [
        "Salut grandpy Comment s est passe ta soiree avec Grandma hier soir "
        "Au fait pendant que j y pense pourrais tu m indiquer ou se trouve "
        "le musee d art et d histoire de Fribourg s il te plait"
    ]

    assert parser.punctuation_and_accent([MENTOR_2]) == [
        "Bonsoir Grandpy j espere que tu as passe une belle semaine Est ce que"
        " tu pourrais m indiquer l adresse de la tour eiffel Merci d avance "
        "et salutations a Mamie"
    ]


def test_prepare():
    assert parser.prepare(OCR_QUESTION) == [" openclassrooms "]

    assert parser.prepare(MENTOR_1) == [
        " soiree grandma hier soir",
        " trouve musee art histoire fribourg plait",
    ]

    assert parser.prepare(MENTOR_2) == [
        " espere belle semaine indiquer tour eiffel " "avance salutations mamie"
    ]

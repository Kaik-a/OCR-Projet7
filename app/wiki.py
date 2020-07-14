"""Media wiki interface"""
import re
from difflib import get_close_matches
from random import choice
from typing import Dict, List, Union

import requests

NULL_ANSWER = (
    "Quoi!? C'est quoi ce charabia? Je comprends rien à votre "
    "language de jeuns, tu peux poser ta question correctement ?"
)

INTRODUCTION: List = [
    "Ça me rappelle une histoire.",
    "Tu sais?",
    "Quand j'était plus jeune, on m'a dit que:",
    "Au fait.",
]


def get_info_on_loc(locations: List[Dict], parsed: List) -> Union[str, List]:
    """
    Get information of a place by using its location.

    :param locations: locations to search for
    :param parsed: title to compare
    :return: Union[str, List]
    """
    results = [
        requests.get(
            "https://fr.wikipedia.org/w/api.php",
            {
                "action": "query",
                "list": "geosearch",
                "format": "json",
                "gscoord": f"{location['lat']}|{location['lng']}",
            },
        ).json()["query"]["geosearch"]
        for location in locations
    ]

    possible_matches: List = [
        [match["title"] for match in result] for result in results
    ]

    if len(results) >= 1 and possible_matches[0]:
        best_match: str = get_close_matches(parsed[0], possible_matches[0], 1)

        # Select first best_match if exist, otherwise take first possible match
        if best_match:
            best_match = best_match[0]
        else:
            best_match = possible_matches[0][0]

        return get_summary(
            [result for result in results[0] if result["title"] == best_match].pop()
        )
    else:
        return NULL_ANSWER


def get_summary(page: Dict) -> str:
    """
    Get summary from wikipedia.

    :param page: page to find the summary
    :return: str summary
    """
    fullpage = requests.get(
        "https://fr.wikipedia.org/w/api.php",
        {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": f"{page['title']}",
        },
    )
    fulltext = fullpage.json()["query"]["pages"][f'{page["pageid"]}']["extract"]

    summary = fulltext.split("<h2>")[0]

    pattern = "([<].*?[>])"

    return re.sub(pattern, "", summary)


def endow(summary: str) -> str:
    """
    Grandpy loves to endow. When he has an answer, he'll tell a story about it.

    :param str summary: summary of the subject found on wiki.
    :return: str
    """

    if summary == NULL_ANSWER:
        return summary

    return f"{choice(INTRODUCTION)} {summary}"

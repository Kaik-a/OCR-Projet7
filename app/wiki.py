"""Media wiki interface"""
from random import choice
import re
import requests
from typing import Dict, List, Union


def get_info_on_loc(locations: List[Dict]) -> Union[str, List]:
    """
    Get information of a place by using its location.

    :param locations: locations to search for
    :return: Union[str, List]
    """
    results = [
        requests.get(
            "https://fr.wikipedia.org/w/api.php",
            {
             "action": "query",
             "list": "geosearch",
             "format": "json",
             "gscoord": f"{location['lat']}|{location['lng']}"
            }).json()['query']['geosearch'] for location in locations
    ]
    if len(results) == 1:
        return get_summary(results[0][0])
    elif not results:
        print("Quoi!? C'est quoi ce charabia? Je comprends rien à votre "
              "language de jeuns, tu peux poser ta question correctement ?")
    else:
        places_found = [
            (index, result[0])
            for index, result in enumerate(results)
        ]
        return get_summary(multiple_choices(places_found))


def get_summary(page: Dict) -> str:
    """
    Get summary from wikipedi.

    :param page: page to find the summary
    :return: str summary
    """
    fullpage = requests.get(
        'https://fr.wikipedia.org/w/api.php',
        {'action': 'query',
         'format': 'json',
         'prop': 'extracts',
         'titles': f"{page['title']}"}
    )
    fulltext = fullpage.json()['query']['pages'][f'{page["pageid"]}']['extract']
    summary = fulltext.split('<h2>')[0]
    pattern = "([<].*?[>])"
    return re.sub(pattern, '', summary)


def endow(summary: str) -> str:
    """
    Grandpy loves to endow. When he has an answer, he'll tell a story about it.

    :param str summary: summary of the subject found on wiki.
    :return: str
    """
    introduction: List = [
        "Ça me rappelle une histoire.",
        "Tu sais?",
        "Quand j'était plus jeune, on m'a dit que:",
        "Au fait.",
    ]

    return f"{choice(introduction)} {summary}"


def multiple_choices(choices: List) -> Dict:
    """
    When the sentence contains multiple questions help grandpy to found the
    good one.

    :param List choices: List of places found.
    :return: Dict
    """
    print(f"Tu parles de tout et de rien, tu cherches quoi exactement?")
    for place in choices:
        print(f'{place[0]} - {place[1]["title"]}')
    answer = input("Tape le chiffre de ce que tu recherches: ")
    try:
        answer = int(answer)
        if answer in range(len(choices)):
            return choices[answer][1]
    except ValueError:
        pass

    print(f"Tu as tapé {answer}, tu vois bien que ça fait pas partie"
          f" des choix proposés? De mon temps, on savait lire au moins!")

    return multiple_choices(choices)

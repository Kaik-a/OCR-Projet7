"""Media wiki interface"""
from difflib import get_close_matches
from random import choice
import re
import requests
from typing import Dict, List, Union


def get_info_on_loc(locations: List[Dict],
                    parsed: List[Dict]) -> Union[str, List]:
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
    possible_matches: List = [
        [match['title'] for match in result] for result in results
    ]
    if len(results) == 1:
        best_match: str = get_close_matches(
            parsed[0],
            possible_matches[0],
            1
        )[0]
        return get_summary(
            [
                result for result in results[0]
                if result['title'] == best_match
            ].pop()
        )
    elif not results:
        print("Quoi!? C'est quoi ce charabia? Je comprends rien à votre "
              "language de jeuns, tu peux poser ta question correctement ?")
    else:
        i = 0
        best_matches = []
        for parse in parsed:
            best_match = get_close_matches(
                    parse, possible_matches[i], 1
                )
            if best_match:
                best_matches.append(best_match[0])
            else:
                best_matches.append(possible_matches[i][0])
            i += 1

        places_found = [
            (index, result)
            for index, result in enumerate(best_matches)
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

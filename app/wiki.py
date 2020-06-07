"""Media wiki interface"""
from random import choice
from typing import Dict, List, Union

from mediawiki import MediaWiki


def get_info_on_loc(locations: List[Dict]) -> Union[str, List]:
    """
    Get information of a place by using its location.

    :param locations: locations to search for
    :return: Union[str, List]
    """
    wiki: MediaWiki = MediaWiki(lang=u'fr')

    results = [wiki.geosearch(latitude=location['lat'],
                              longitude=location['lng'],
                              results=1) for location in locations]

    if len(results) == 1:
        return wiki.page(results[0][0]).summary
    elif not results:
        print("Quoi!? C'est quoi ce charabia? Je comprends rien à votre "
              "language de jeuns, tu peux poser ta question correctement ?")
    else:
        places_found = [
            (index, wiki.page(result[0]))
            for index, result in enumerate(results)
        ]
        return multiple_choices(places_found).summary


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


def multiple_choices(choices: List) -> MediaWiki:
    """
    When the sentence contains multiple questions help grandpy to found the
    good one.

    :param List choices: List of places found.
    :return: Mediawiki
    """
    print(f"Tu parles de tout et de rien, tu cherches quoi exactement?")
    for place in choices:
        print(f'{place[0]} - {place[1].title}')
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

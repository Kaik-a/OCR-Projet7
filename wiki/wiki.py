"""Media wiki interface"""
from typing import Dict

from mediawiki import MediaWiki


def get_info_on_loc(location: Dict):
    """
    Get information of a place by using its location.

    :param location: location to search for
    :return: str
    """
    wiki: MediaWiki = MediaWiki(lang=u'fr')

    result = wiki.geosearch(latitude=location['lat'],
                       longitude=location['lng'],
                       auto_suggest=True)

    return wiki.page(result[0]).summary





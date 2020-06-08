"""File containing the parser for question. """

from re import findall, sub
from typing import List

QUESTION_START = [
    "quel",
    "quelle",
    "quels",
    "quelles",
    "où",
    "ou",
    "comment"
]

test = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? " \
       "Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le" \
       " musée d'art et d'histoire de Fribourg, s'il te plaît?"

test2 = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce " \
        "que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci " \
        "d'avance et salutations à Mamie."


def parse(to_parse: str) -> List:
    """
    Find in the phrase asked to the bot if there's a question pattern in it.
    If there's questions pattern, return it. Otherwise return all the sentence
    in a List.

    :param str to_parse: sentence asked to bot.
    :return: List
    """
    to_parse = to_parse.lower()
    pattern = r'((\bquel|\bquelle|\bquels|\bquelles|\bou|\boù|\bcomment).*?[?])'
    matches = findall(pattern, to_parse)
    parsed = [match[0] for match in matches]
    if parsed:
        return parsed
    else:
        return [to_parse]


def unclutter(questions: list) -> List:
    """
    Remove from questions all the words from stopwords.

    :param List questions: questions asked.
    :return: List
    """
    for index, question in enumerate(questions):
        for stopword in stopwords:
            question = sub(r'\b' + f'{stopword}' r'\b ', ' ', question)
        questions[index] = question
        # remove multiple contiguous spaces
        questions[index] = sub(' {2,}', ' ', question)
    return questions


def punctuation_and_accent(questions: List):
    """
    Remove all the punctuation and accents from questions.

    :param List questions: questions asked.
    :return: List
    """
    for index, question in enumerate(questions):
        # accents
        question = sub('[éèê]', 'e', question)
        question = sub('[àâ]', 'a', question)
        question = sub('ô', 'o', question)
        question = sub('ù', 'u', question)
        question = sub('î', 'i', question)
        # punctuation
        question = sub('\'', ' ', question)
        question = sub('-', ' ', question)
        question = sub('[()@&é"§!°_$*€^¨%`£=+:/;.?,]', '', question)

        questions[index] = question

    return questions


stopwords = {'a', 'abord', 'absolument', 'afin', 'ah', 'ai', 'aie', 'ailleurs',
             'ainsi', 'ait', 'allaient', 'allo', 'allons', 'allo', 'alors',
             'anterieur', 'anterieure', 'anterieures', 'apres', 'apres', 'as',
             'assez', 'attendu', 'au', 'aucun', 'aucune', 'aujourd',
             'aujourdhui', 'aupres', 'auquel', 'aura', 'auraient', 'aurait',
             'auront', 'aussi', 'autre', 'autrefois', 'autrement', 'autres',
             'autrui', 'aux', 'auxquelles', 'auxquels', 'avaient', 'avais',
             'avait', 'avant', 'avec', 'avoir', 'avons', 'ayant', 'b', 'bah',
             'bas', 'basee', 'bat', 'beau', 'beaucoup', 'bien', 'bigre', 'boum',
             'bravo', 'brrr', 'c', 'car', 'ce', 'ceci', 'cela', 'celle',
             'celle-ci', 'celle-la', 'celles', 'celles-ci', 'celles-la',
             'celui', 'celui-ci', 'celui-la', 'cent', 'cependant', 'certain',
             'certaine', 'certaines', 'certains', 'certes', 'ces', 'cet',
             'cette', 'ceux', 'ceux-ci', 'ceux-la', 'chacun', 'chacune',
             'chaque', 'cher', 'chers', 'chez', 'chiche', 'chut', 'chere',
             'cheres', 'ci', 'cinq', 'cinquantaine', 'cinquante',
             'cinquantieme', 'cinquieme', 'clac', 'clic', 'combien', 'comme',
             'comment', 'comparable', 'comparables', 'compris', 'concernant',
             'contre', 'couic', 'crac', 'd', 'da', 'dans', 'de', 'debout',
             'dedans', 'dehors', 'deja', 'dela', 'depuis', 'dernier',
             'derniere', 'derriere', 'derriere', 'des', 'desormais',
             'desquelles', 'desquels', 'dessous', 'dessus', 'deux', 'deuxieme',
             'deuxiemement', 'devant', 'devers', 'devra', 'different',
             'differentes', 'differents', 'different', 'differente',
             'differentes', 'differents', 'dire', 'directe', 'directement',
             'dit', 'dite', 'dits', 'divers', 'diverse', 'diverses', 'dix',
             'dix-huit', 'dix-neuf', 'dix-sept', 'dixieme', 'doit', 'doivent',
             'donc', 'dont', 'douze', 'douzieme', 'dring', 'du', 'duquel',
             'durant', 'des', 'desormais', 'e', 'effet', 'egale', 'egalement',
             'egales', 'eh', 'elle', 'elle-meme', 'elles', 'elles-memes', 'en',
             'encore', 'enfin', 'entre', 'envers', 'environ', 'es', 'est', 'et',
             'etant', 'etc', 'etre', 'eu', 'euh', 'eux', 'eux-memes',
             'exactement', 'excepte', 'extenso', 'exterieur', 'f', 'fais',
             'faisaient', 'faisant', 'fait', 'façon', 'feront', 'fi', 'flac',
             'floc', 'font', 'g', 'gens', 'grandpy', 'h', 'ha', 'hein', 'hem',
             'hep', 'hi',
             'ho', 'hola', 'hop', 'hormis', 'hors', 'hou', 'houp', 'hue', 'hui',
             'huit', 'huitieme', 'hum', 'hurrah', 'he', 'helas', 'i', 'il',
             'ils', 'importe', 'j', 'je', 'jusqu', 'jusque', 'juste', 'k', 'l',
             'la', 'laisser', 'laquelle', 'las', 'le', 'lequel', 'les',
             'lesquelles', 'lesquels', 'leur', 'leurs', 'longtemps', 'lors',
             'lorsque', 'lui', 'lui-meme', 'lui-meme', 'la', 'les', 'm', 'ma',
             'maint', 'maintenant', 'mais', 'malgre', 'malgre', 'maximale',
             'me', 'meme', 'memes', 'merci', 'mes', 'mien', 'mienne', 'miennes',
             'miens', 'mille', 'mince', 'minimale', 'moi', 'moi-meme',
             'moi-meme', 'moindres', 'moins', 'mon', 'moyennant', 'multiple',
             'multiples', 'meme', 'memes', 'n', 'na', 'naturel', 'naturelle',
             'naturelles', 'ne', 'neanmoins', 'necessaire', 'necessairement',
             'neuf', 'neuvieme', 'ni', 'nombreuses', 'nombreux', 'non', 'nos',
             'notamment', 'notre', 'nous', 'nous-memes', 'nouveau', 'nul',
             'neanmoins', 'notre', 'notres', 'o', 'oh', 'ohe', 'olle', 'ole',
             'on', 'ont', 'onze', 'onzieme', 'ore', 'ou', 'ouf', 'ouias',
             'oust', 'ouste', 'outre', 'ouvert', 'ouverte', 'ouverts', 'o|',
             'ou', 'p', 'paf', 'pan', 'par', 'parce', 'parfois', 'parle',
             'parlent', 'parler', 'parmi', 'parseme', 'partant', 'particulier',
             'particuliere', 'particulierement', 'pas', 'passe', 'pendant',
             'pense', 'permet', 'personne', 'peu', 'peut', 'peuvent', 'peux',
             'pff', 'pfft', 'pfut', 'pif', 'pire', 'plein', 'plouf', 'plus',
             'plusieurs', 'plutot', 'possessif', 'possessifs', 'possible',
             'possibles', 'pouah', 'pour', 'pourquoi', 'pourrais', 'pourrait',
             'pouvait', 'prealable', 'precisement', 'premier', 'premiere',
             'premierement', 'pres', 'probable', 'probante', 'procedant',
             'proche', 'pres', 'psitt', 'pu', 'puis', 'puisque', 'pur', 'pure',
             'q', 'qu', 'quand', 'quant', 'quant-a-soi', 'quanta', 'quarante',
             'quatorze', 'quatre', 'quatre-vingt', 'quatrieme', 'quatriemement',
             'que', 'quel', 'quelconque', 'quelle', 'quelles', 'quelquun',
             'quelque', 'quelques', 'quels', 'qui', 'quiconque', 'quinze',
             'quoi', 'quoique', 'r', 'rare', 'rarement', 'rares', 'relative',
             'relativement', 'remarquable', 'rend', 'rendre', 'restant',
             'reste', 'restent', 'restrictif', 'retour', 'revoici', 'revoila',
             'rien', 's', 'sa', 'sacrebleu', 'sait', 'sans', 'sapristi', 'sauf',
             'se', 'sein', 'seize', 'selon', 'semblable', 'semblaient',
             'semble', 'semblent', 'sent', 'sept', 'septieme', 'sera',
             'seraient', 'serait', 'seront', 'ses', 'seul', 'seule',
             'seulement', 'si', 'sien', 'sienne', 'siennes', 'siens', 'sinon',
             'six', 'sixieme', 'soi', 'soi-meme', 'soit', 'soixante', 'son',
             'sont', 'sous', 'souvent', 'specifique', 'specifiques',
             'speculatif', 'stop', 'strictement', 'subtiles', 'suffisant',
             'suffisante', 'suffit', 'suis', 'suit', 'suivant', 'suivante',
             'suivantes', 'suivants', 'suivre', 'superpose', 'sur', 'surtout',
             't', 'ta', 'tac', 'tant', 'tardive', 'te', 'tel', 'telle',
             'tellement', 'telles', 'tels', 'tenant', 'tend', 'tenir', 'tente',
             'tes', 'tic', 'tien', 'tienne', 'tiennes', 'tiens', 'toc', 'toi',
             'toi-meme', 'ton', 'touchant', 'toujours', 'tous', 'tout', 'toute',
             'toutefois', 'toutes', 'treize', 'trente', 'tres', 'trois',
             'troisieme', 'troisiemement', 'trop', 'tres', 'tsoin', 'tsouin',
             'tu', 'te', 'u', 'un', 'une', 'unes', 'uniformement', 'unique',
             'uniques', 'uns', 'v', 'va', 'vais', 'vas', 'vers', 'via', 'vif',
             'vifs', 'vingt', 'vivat', 'vive', 'vives', 'vlan', 'voici',
             'voila', 'vont', 'vos', 'votre', 'vous', 'vous-memes', 'vu', 've',
             'votre', 'votres', 'w', 'x', 'y', 'z', 'zut', 'a', 'a', 'ça', 'es',
             'etaient', 'etais', 'etait', 'etant', 'ete', 'etre', 'o'}


def prepare(sentence: str) -> List:
    """
    Prepare sentence to call google api.

    :param sentence: sentence asked to the bot.
    :return: List
    """
    parsed = parse(sentence)
    formatted = punctuation_and_accent(parsed)

    return unclutter(formatted)


# print(prepare(test), '\n', prepare(test2))

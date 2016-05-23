""" This module parses coffee names to find the following attributes: decaf, organic, fair trade, 
their country and a descriptive adjective.
"""

from collections import OrderedDict

COUNTRIES = {
    'BALINESE':     'BALI',
    'BOLIVIAN':     'BOLIVIA',
    'BRAZILIAN':    'BRAZIL',
    'COSTA RICAN':  'COSTA RICA',
    'DOMINICAN':    'DOMINICAN REPUBLIC',
    'SALVADOREAN':  'EL SALVADOR',
    'ETHIOPIAN':    'ETHIOPIA',
    'GUATEMALAN':   'GUATEMALA',
    'INDIAN':       'INDIA',
    'KENYAN':       'KENYA',
    'MALIAN':       'MALI',
    'MEXICAN':      'MEXICO',
    'PANAMANIAN':   'PANAMA',
    'PERUVIAN':     'PERU',
    'SUMATRAN':     'SUMATRA',
}

def tryToRemove(parsed_name, string_to_remove):
    """ This method tries to find `string_to_remove` in `parsed_name` and returns whether it was 
    found, while also removing it in place from `parsed_name` if it does.
    """

    string_list = string_to_remove.split(' ')
    for string in string_list:
        try:
            parsed_name.remove(string.upper())
            string_present = 'True'
        except:
            string_present = 'False'
    return string_present

def parse(name):
    parsed_name = map(str.upper, name.split(' '))
    decaf = tryToRemove(parsed_name, 'decaf')
    organic = tryToRemove(parsed_name, 'organic')
    fair_trade = tryToRemove(parsed_name, 'fair trade')
    try:
        country = COUNTRIES[parsed_name[-1]]
        parsed_name = parsed_name[:-1]
    except KeyError:
        country = COUNTRIES[' '.join(parsed_name[-2:])]
        parsed_name = parsed_name[:-2]
    adjective = ' '.join(parsed_name)
    keys = map(str.title, 'decaf,organic,fair trade,country,adjective'.split(','))
    values = (decaf, organic, fair_trade, country.title(), adjective.title())
    return OrderedDict(zip(keys, values))
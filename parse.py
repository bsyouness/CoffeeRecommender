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
    string_list = string_to_remove.split(' ')
    for string in string_list:
        try:
            parsed_name.remove(string.upper())
            string_present = True
        except:
            string_present = False
    return string_present

def parse(name):
    parsed_name = map(str.upper, name.split(' '))
    decaf = tryToRemove(parsed_name, 'decaf')
    organic = tryToRemove(parsed_name, 'organic')
    fair_trade = tryToRemove(parsed_name, 'fair trade')
    try:
        country = COUNTRIES[parsed_name[-1]]
        parsed_name = parsed_name[:-1]
    except:
        country = COUNTRIES[' '.join(parsed_name[-2:])]
        parsed_name = parsed_name[:-2]
    adjective = ' '.join(parsed_name)
    keys = map(str.title, 'decaf,organic,fair trade,country,adjective'.split(','))
    values = (decaf, organic, fair_trade, country.title(), adjective.title())
    return {key: value for (key, value) in zip(keys, values)}
import pandas as pd
import parse

def addIndent(string):
    split_string = string.split('\n')
    return '\n'.join([split_string[0]] + map(lambda x: '   ' + x, split_string[1:]))

def summarize(df):
    ratings_by_userid = df.groupby('userid')
    ratings_by_coffee_name = df.groupby('coffee_name')
    user_stats = 'There is a total of {} users'.format(len(ratings_by_userid))
    coffee_stats = 'There is a total of {} coffee names'.format(len(ratings_by_coffee_name))
    
    coffee_names = ratings_by_coffee_name.groups.keys()
    coffee_names_df = pd.DataFrame(map(parse.parse, coffee_names))
    decaf_stats, fair_trade_stats, organic_stats, adj_stats, country_stats = \
        coffee_names_df.groupby('Decaf').size().to_string(), \
        coffee_names_df.groupby('Fair Trade').size().to_string(), \
        coffee_names_df.groupby('Organic').size().to_string(), \
        coffee_names_df.groupby('Adjective').size().to_string(), \
        coffee_names_df.groupby('Country').size().to_string()
    
    separator = 2*'\n' 
    print separator.join([user_stats] + [coffee_stats] + map(addIndent, [decaf_stats, \
        fair_trade_stats, organic_stats, adj_stats, country_stats]))
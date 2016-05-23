""" This script allows to:
1) Parse names based on a certain structure:
```
$ python coffee.py parse "Organic Fair Trade Sweet and Sour Indian"
Decaf                    False
Organic                   True
Fair Trade                True
Country                  India
Adjective       Sweet And Sour
```

2) Summarize data in a text file:
```
$ python coffee.py summarize "coffee_ratings.txt" 
There are a total of 200 users

There are a total of 189 coffee names

Decaf
   False     89
   True     100

Fair Trade
   False    110
   True      79

Organic
   False     89
   True     100

Adjective
   Aa                 14
   Black Satin        13
   ...

Country
   Bali                  16
   Bolivia               15
   ...
```

3) Recommend 3 new items based on user data from a text file:
```
$ python coffee.py recommend "coffee_ratings.txt" 
uid coffee name                                       inferred rating


0   daysiss Water Salvadorean                            4
0   Organic Fair Trade Decaf Black Satin Bolivian        3
0   Fair Trade Honey Burst Peruvian                      3
...
```
"""

from __future__ import print_function
import argparse
import parse
import summarize
import collaborative_filtering as cf

class Coffee(object):
    def __init__(self, name, parsed_name={}):
        self.name = name
        self.parsed_name = parsed_name

    def display(self):
        [print('{:<15}{:>15}'.format(key, value)) for (key, value) in self.parsed_name.items()]
    
    @classmethod
    def fromname(cls, name):
        return cls(name, parse.parse(name))


def main():
    # Create a parser object to handle passing arguments through the command line
    parser = argparse.ArgumentParser(description='TextNow Coffee Tasting')
    subparsers = parser.add_subparsers(dest='command', help='command')

    # Define 3 parser objects for the 3 different operations that are available
    commands = ['parse', 'summarize', 'recommend']
    parsers = {c: subparsers.add_parser(c) for c in commands}
    parsers['parse'].add_argument('arg', help='coffee descriptive name')
    parsers['summarize'].add_argument('arg', help='input csv file',
                                      type=argparse.FileType('r'))
    parsers['recommend'].add_argument('arg', help='input csv file',
                                      type=argparse.FileType('r'))
    args = parser.parse_args()
    
    if args.command == 'parse':
        coffee = Coffee.fromname(name=args.arg)
        coffee.display()
           
    if args.command == 'summarize':
        summarize.summarize(args.arg)

    if args.command == 'recommend':
        cf.recommend(args.arg)


if __name__ == '__main__':
    main()
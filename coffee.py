""" This script allows to:
1) Parse names based on a certain structure:
```
$ python coffee.py parse "Organic Decaf Mandeheling Bolivian"                    

Decaf      True
Organic    True
Fair trade False
Adjective  Mandheling
Country    Bolivia
```

2) Summarize data in a text file:
```
$ python coffee.py summarize coffee_ratings.txt

Total people 140
Total coffee types 50
Decaf               
  True 20               
  False 30
Organic             
  True 10               
  False 40
Fair trade              
  True 5                
  False 45
Adjective               
  Bright 15             
  Supremo 35
Country             
  India 10
  Peru 40
```

3) Recommend 3 new items based on user data from a text file:
```
$ python coffee.py recommend coffee_ratings.txt

userid coffee name inferred rating
9 Decaf Black Satin Balinese 4
9 Black Satin Balinese 4
9 Organic Longberry Mexican 4
10 Honey Burst Domincan 5
10 Organic Fair Trade AA Guatemalan 4
10 Organic Fair Trade Decaf Swiss Water Malian 4
```
"""

from __future__ import print_function
import argparse
import parse
import summarize
import collaborative_filtering as cf

class Coffee(object):
    def __init__(self, name='Fair Trade Decaf Black Satin Panamanian', parsed_name={}):
        self.name = name
        self.parsed_name = parsed_name

    def display(self):
        [print('{:<15}{:>15}'.format(key, value)) for (key, value) in self.parsed_name.items()]
    
    @classmethod
    def fromname(cls, name='Fair Trade Decaf Black Satin Panamanian'):
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
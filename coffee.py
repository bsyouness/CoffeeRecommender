from __future__ import print_function
import argparse
import parse
import summarize
import collaborative_filtering as cf

'''
get MS Visual C++ 9.0 @ http://aka.ms/vcpython27
install pandas
install pyreadline as well as ipython
pip install matplotlib
'''

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
    parser = argparse.ArgumentParser(description='TextNow Coffee Tasting')
    subparsers = parser.add_subparsers(dest='command', help='command')

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
        cf.recommend()


if __name__ == '__main__':
    main()
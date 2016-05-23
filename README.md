# Coffee Recommender

## Introduction

This repository contains code to parse coffee names based on a certain structure, summarize user rating data from a text file, and recommend new coffees to users. This is a coding challenge for [TextNow](https://www.textnow.com/). 

## Running the code

To install the dependencies, execute the following commands `pip install -r requirements.txt`.

## Challenge Summary

The repo contains four executables. The main, `coffee.py` is called from the command line, and runs `parse.py`, `summarize.py`, or `collaborative_filtering.py`, depending on the user input.

### Parse

Use `parse.py` to parse names based on a certain structure:
```
$ python coffee.py parse "Organic Fair Trade Sweet and Sour Indian"
Decaf                    False
Organic                   True
Fair Trade                True
Country                  India
Adjective       Sweet And Sour
```
### Summarize

Use `summarize.py` to summarize data in a text file:
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
   Caturra            16
   Cuzcachapa         15
   Daysiss Water       1
   Honey Burst        15
   Longberry          10
   Mandheling          9
   Paradise Valley    18
   Peaberry           17
   Reserve            12
   Sidamo             14
   Supremo            18
   Swiss Water        17

Country
   Bali                  16
   Bolivia               15
   Brazil                15
   Costa Rica            10
   Dominican Republic    13
   El Salvador           16
   Ethiopia               9
   Guatemala             11
   India                 16
   Kenya                 10
   Mali                  12
   Mexico                 4
   Panama                14
   Peru                  15
   Sumatra               13
```

### Recommend
Use `collaborative_filtering.py` to recommend 3 new items based on user data from a text file:
```
$ python coffee.py recommend "coffee_ratings.txt" 
uid coffee name                                       inferred rating


0   daysiss Water Salvadorean                            4
0   Organic Fair Trade Decaf Black Satin Bolivian        3
0   Fair Trade Honey Burst Peruvian                      3


1   Organic Fair Trade Decaf Black Satin Balinese        4
1   Organic Fair Trade Decaf Paradise Valley Malian      4
1   Organic Fair Trade Decaf Paradise Valley Kenyan      4


2   daysiss Water Salvadorean                            4
2   Organic Decaf Sidamo Panamanian                      3
2   Organic Decaf AA Guatemalan                          3


3   daysiss Water Salvadorean                            4
3   Organic Fair Trade Decaf Black Satin Bolivian        3
3   Fair Trade Decaf Swiss Water Sumatran                3
```

### To do: 

Do a proper train/test split to test the generalizability of the collaborative filtering code. 
Add unittests for all methods in the repo. And add Travis.
Improve comments.
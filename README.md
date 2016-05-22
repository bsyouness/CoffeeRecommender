# Coffee Recommender

## Introduction

This repository contains code to parse coffee names based on a certain structure, summarize user rating data from a text file, and recommend new coffees to users. This is a coding challenge for [TextNow](https://www.textnow.com/). 

## Running the code

To install the dependencies, execute the following commands:

    pip install -r requirements.txt

## Challenge Summary

The repo contains four executables. The `main` -- `coffee.py` -- is called from the comamand line, and runs `parse.py`, `summarize.py`, or `collaborative_filtering.py`, depending on the user input.

### Parse

Use `parse.py` to parse names based on a certain structure:
```
$ python coffee.py parse "Organic Decaf Mandeheling Bolivian"                    

Decaf      True
Organic    True
Fair trade False
Adjective  Mandheling
Country    Bolivia
```
### Summarize

Use `summarize.py` to summarize data in a text file:
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

### Recommend
Use `collaborative-filtering.py` to recommend 3 new items based on user data from a text file:
```
$ python coffee.py recommend coffee_ratings.txt
userid coffee name inferred rating
9 Decaf Black Satin Baalinese 4
9 Black Satin Balinese 4
9 Organic Longberry Mexican 4
10 Honey Burst Domincan 5
10 Organic Fair Trade AA Guatemalan 4
10 Organic Fair Trade Decaf Swiss Water Malian 4
```

### To do: 

Add tests.
Add Travis.
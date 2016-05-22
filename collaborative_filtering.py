"""
This script implements a collaborative filtering algortithm using the Pearson correlation coefficient
to avoid issues with scaling in the ratings of the users.
(https://www.wikiwand.com/en/Pearson_product-moment_correlation_coefficient)

This code is based on the blog:
https://dataaspirant.com/2015/05/25/collaborative-filtering-recommendation-engine-implementation-in-python/

Readings: 
  http://www.salemmarafi.com/code/collaborative-filtering-r/ 
"""

import pandas as pd 

def pearsonCorrelation(p1_data, p2_data, p1_items, p2_items):
  """ Computes the Pearson correlation coefficient between the rating data from 2 people. 
  The rating data is in the form of a pandas dataframe with two columns; the first columns is the keys 
  of the dataframe, the second columns contains the ratings for each item and is named `rating`.

  Args:
    p1_data: Pandas dataframe containing the rating data for the first person
    p2_data: Pandas dataframe containing the rating data for the second person
    p1_items: Pandas series containing the items rated by the first person
    p2_items: Pandas series containing the items rated by the second person  

  Returns:
    The Pearson correlation value for the pair of data inputted. 
  """

  # Checking for number of ratings in common
  if p1_items == p2_items:
    both_rated = p1_items
  else:
    both_rated = []
    for item in p1_items:
      if item in p2_items:
        both_rated.append(item)
  n = len(both_rated) 
  
  # If the two people have no ratings in common
  if n == 0:
    return 0

  # Sum all the preferences of each person
  p1_preferences_sum = sum([p1_data['rating'][item] for item in both_rated])
  p2_preferences_sum = sum([p2_data['rating'][item] for item in both_rated])
  
  # Sum the squares of preferences of each person
  p1_square_preferences_sum = sum([pow(p1_data['rating'][item],2) for item in both_rated])
  p2_square_preferences_sum = sum([pow(p2_data['rating'][item],2) for item in both_rated])

  # Calculate the sum product of the rating for each item for person 1 and person 2 
  p1_p2_sumproduct = sum([p1_data['rating'][item] * p2_data['rating'][item] for item in both_rated])

  # Calculate the Pearson correlation coefficient
  numerator_value = p1_p2_sumproduct - (p1_preferences_sum*p2_preferences_sum/n)
  denominator_value = pow((p1_square_preferences_sum - pow(p1_preferences_sum,2)/n)* \
                          (p2_square_preferences_sum - pow(p2_preferences_sum,2)/n), .5)
  
  if denominator_value == 0:
    return 0
  else:
    return numerator_value/denominator_value

def userRecommendation(p1, column_name, grouped_df):
  """ Gets recommendations for a person by using a weighted average of every other user's rankings
  """
  totals = {}
  similarity_sums = {}
  rankings_list =[]
  all_people = grouped_df.groups.keys()
  
  for p2 in all_people:
    # Don't compare the same user to himself
    if p1 == p2:
      continue

    p1_data = grouped_df.get_group(p1).set_index(column_name)
    p2_data = grouped_df.get_group(p2).set_index(column_name)
    p1_items = sorted(p1_data.index)
    p2_items = sorted(p2_data.index)

    similarity_score = pearsonCorrelation(p1_data, p2_data, p1_items, p2_items)

    # Ignore scores of zero or lower
    if similarity_score <= 0:
      continue
    
    for item in p2_items:
      # Only score items person p1 hasn't rated yet
      if item not in p1_items:
        totals.setdefault(item, 0)
        totals[item] += p2_data['rating'][item] * similarity_score
        similarity_sums.setdefault(item, 0)
        similarity_sums[item] += similarity_score

  # Create the list of recommended items in decreasing order of rating for person p1 with a
  # rating based on the normalized ratings of the other users
  rankings = [(p1, item, int(total/similarity_sums[item])) for item, total in totals.items()]
  rankings.sort(key=lambda t: t[2])
  rankings.reverse()
  
  # Return the 3 top recommended items
  return rankings[:3]

def recommend(f):
  ratings = pd.read_table(f, names = ['userid', 'coffee_name', 'rating'])
  ratings.drop_duplicates(subset=['userid', 'coffee_name'], keep = 'first', inplace = True)
  ratings_by_userid = ratings.groupby('userid')
  all_people = ratings_by_userid.groups.keys()  
  format_string = '{:<4}{:<50}{:>4}'
  print(format_string.format('uid', 'coffee name', 'inferred rating'))
  for p1 in all_people:
    print('\n')
    recommendations = userRecommendation(p1, 'coffee_name', ratings_by_userid)
    for (p, c, r) in recommendations:
      print(format_string.format(p, c, r))
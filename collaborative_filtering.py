import pandas as pd 

# http://www.salemmarafi.com/code/collaborative-filtering-r/ inspired by: https://dataaspirant.com/2015/05/25/collaborative-filtering-recommendation-engine-implementation-in-python/
def pearsonCorrelation(p1_data, p2_data, p1_items, p2_items, column_name, grouped_df):
  #Pearson correlation and cosine similarity are invariant to scaling, i.e. multiplying all elements by a nonzero constant. Pearson correlation is also invariant to adding any constant to all elements To get both rated items
  # we can assume in this case that all users have rated all coffees
  if p1_items == p2_items:
    both_rated = p1_items
  else:
    both_rated = []
    for item in p1_items:
      if item in p2_items:
        both_rated.append(item)

  n = len(both_rated) 

  # Checking for number of ratings in common
  if n == 0:
    return 0

  # Add up all the preferences of each user
  p1_preferences_sum = sum([p1_data['rating'][item] for item in both_rated])
  p2_preferences_sum = sum([p2_data['rating'][item] for item in both_rated])
  
  # Sum up the squares of preferences of each user
  p1_square_preferences_sum = sum([pow(p1_data['rating'][item],2) for item in both_rated])
  p2_square_preferences_sum = sum([pow(p2_data['rating'][item],2) for item in both_rated])

  # Sum up the product value of both preferences for each item
  p1_p2_sumproduct = sum([p1_data['rating'][item] * p2_data['rating'][item] for item in both_rated])

  # Calculate the pearson score
  numerator_value = p1_p2_sumproduct - (p1_preferences_sum*p2_preferences_sum/n)
  denominator_value = pow((p1_square_preferences_sum - pow(p1_preferences_sum,2)/n)* \
                          (p2_square_preferences_sum - pow(p2_preferences_sum,2)/n), .5)
  
  if denominator_value == 0:
    return 0
  else:
    return numerator_value/denominator_value

def userRecommendation(p1, column_name, grouped_df):
  # Gets recommendations for a person by using a weighted average of every other user's rankings
  totals = {}
  similarity_sums = {}
  rankings_list =[]
  all_people = grouped_df.groups.keys()
  
  for p2 in all_people:
    # Don't compare the same user to himself to myself
    if p1 == p2:
      continue

    p1_data = grouped_df.get_group(p1).set_index(column_name)
    p2_data = grouped_df.get_group(p2).set_index(column_name)
    p1_items = sorted(p1_data.index)
    p2_items = sorted(p2_data.index)

    similarity_score = pearsonCorrelation(p1_data, p2_data, p1_items, p2_items, column_name, grouped_df)

    # ignore scores of zero or lower
    if similarity_score <= 0:
      continue
    
    for item in p2_items:
    # only score movies i haven't seen yet
      if item not in p1_items:
        # Similrity * score
        totals.setdefault(item, 0)
        totals[item] += p2_data['rating'][item] * similarity_score
        # sum of similarities
        similarity_sums.setdefault(item, 0)
        similarity_sums[item] += similarity_score

  # Create the normalized list
  rankings = [(p1, item, int(total/similarity_sums[item])) for item, total in totals.items()]
  rankings.sort()
  rankings.reverse()
  # returns the recommended items
  return rankings[:3]

def recommend_sub(f):
  ratings = pd.read_table(f, names = ['userid', 'coffee_name', 'rating'])
  ratings.drop_duplicates(subset=['userid', 'coffee_name'], keep = 'first', inplace = True)
  ratings_by_userid = ratings.groupby('userid')
  all_people = ratings_by_userid.groups.keys()  
  for p1 in all_people:
    recommendations = userRecommendation(p1, 'coffee_name', ratings_by_userid)
    for (p, c, r) in recommendations:
      print('{:<15}{:<30}{:>15}'.format(p, c, r))

def recommend():
  f = open('coffee_ratings.txt', 'r')
  recommend_sub(f)

def testing():
  print ('test')
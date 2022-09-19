import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from afinn import Afinn
afinn = Afinn(language='en')
#import everthing you need

#make a procedure that finds the most frequent word in a review
def most_frequent_word_finder(review):
 counter = 0
 review = review.split()
 most_frequent_word = review[0]
 for word in review:
  if len(word) >= 6:
   current_frequency = review.count(word)
   if current_frequency > counter:
    counter = current_frequency
    most_frequent_word = word
 return most_frequent_word

#sentiment analysis
print(afinn.score('I had a bad day yesterday. But today was great.'))

#read a .txt file and save it as a list
file_1 = open("AIV_Reviews.txt","r+")
reviews = []
for line in file_1:
 reviews.append(line)
file_1.close()

file_2 = open("AIV_Metadata.json","r+")
metadata = []
for line in file_2:
 metadata.append(line)
file_2.close()

print(reviews[2])
print()

# START HERE 
import json 

# set JSON to a specific product review
x = reviews[2]
#  divides the program into a small piece of code for analyzing the correct syntax
y = json.loads(x)

# USER ID
print("USER ID:")
# finds "reviewerID" in reviews[1] and prints the corresponding syntax
print(y["reviewerID"])
selected_users_id = y["reviewerID"]
print()

# NAME OF PRODUCT (or in this case, the Amazon ID number)
print("ASIN NUMBER:")
# finds "asin" in reviews[1] and prints the corresponding syntax
print(y["asin"])
selected_users_asin = y["asin"]
print()

# PRODUCT DESCRIPTION (commentary)
print("PRODUCT DESCRIPTION:")
# finds "reviewText" in reviews[1] and prints the corresponding syntax
print(y["reviewText"])
South_Park_review_text = y["reviewText"]
print()

# SENTIMENT ANALYSIS (rating on the 5.0 scale)
print("RATING:")
# finds "overall" in reviews[1] and prints the corresponding syntax
print(y["overall"])
rating = float(y["overall"])
# if the rating is high, the review will be labled as positive
if rating >= 4.0:
  userreview = "positive review"
# if the rating is low, the review will be labled as negative
elif rating <= 2.0:
  userreview = "negative review"
# if the rating is in the middle of the scale, the review will be labled as neutral
else:
  userreview = "neutral review"
# reports the review status
print(userreview)
print()

print('AVERAGE RATING FROM OTHER USERS:') 
rating_list = [] #make a rating list
for review in reviews: #for each review in reviews
 loaded_review = json.loads(review) #load the review
 if loaded_review["asin"] == y["asin"]: #if the asin number is equal the the asin number from the single user's review
  rating_list.append(loaded_review["overall"]) #append the overall rating from the review to the rating list
ratings_sum = sum(rating_list) 
average_rating = ratings_sum / len(rating_list) #find the average of all the ratings in the ratings list

# if the rating is high, the review will be labled as positive
if average_rating >= 4.0:
  average_userreview = "positive review"
# if the rating is low, the review will be labled as negative
elif average_rating <= 2.0:
  average_userreview = "negative review"
# if the rating is in the middle of the scale, the review will be labled as neutral
else:
  average_userreview = "neutral review"
print(average_rating)
print(average_userreview)
if userreview == average_userreview: #if the single user's review is equal to the average review
  print('')
  print("Other reviewers tend to agree with the review of the single user.") #the single user's review is similar to other reviews
else:
  print('')
  print("Other reviewers tend to disagree with the review of the single user.") #the single user's review is dissimilar to other reviews
print()

# searches the complete list of reviews for reviews with this user's specific reviwerID number
print(" PRODUCTS REVIEWED BY SECLECTED USER:")
products_reviwed_by_selected_user = []
for z in range (len(reviews)):
  if selected_users_id in reviews[z]:
    products_reviwed_by_selected_user.append(reviews[z])
    print(products_reviwed_by_selected_user)
    print()

review_text_1 = y["reviewText"]
most_frequent_word = most_frequent_word_finder(review_text_1) #find the most used word in the users review

#find out which reviews have the most frequent word
reviews.remove(reviews[2])
best_products_list_1 = []
for review in reviews: 
 __x__ = review
 __y__ = json.loads(__x__)
 review_text_2 = __y__["reviewText"]
 review_text_2 = review_text_2.split()
 for word in review_text_2:
  if word == most_frequent_word:
    best_products_list_1.append(review)

#find out which of the reviews that have the most frequent word have a rating of 5
best_products_list_2 = []
for review in best_products_list_1:
 __x__ = review
 __y__ = json.loads(__x__)
 rating = __y__["overall"]
 if rating >= 5:
  best_products_list_2.append(review)

#find out which of the reviews that have the most frequent word and rating of 5 have the word "South" in it
best_products_list_3 = []
for review in best_products_list_2:
 __x__ = review
 __y__ = json.loads(__x__)
 review_text_3 = __y__["reviewText"]
 review_text_3 = review_text_3.split()
 for word in review_text_3:
   if word == 'South':
    best_products_list_3.append(review)

#make a list that contains words from the user's review that have at least 5 letters in them
most_notable_words = []
South_Park_review_text = South_Park_review_text.split()
for word in South_Park_review_text:
 if len(word) >= 5:
  most_notable_words.append(word)

#fix if necessary
most_notable_words_fixed = []
for notable_word in most_notable_words:
    if notable_word not in most_notable_words_fixed:
        most_notable_words_fixed.append(notable_word)

#find out which of the reviews have the notable words
best_products_list_4 = []
for review in best_products_list_3:
 __x__ = review
 __y__ = json.loads(__x__)
 review_text_4 = __y__["reviewText"]
 review_text_4 = review_text_4.split()
 for word in review_text_4:
  for notable_word in most_notable_words_fixed:
   if word == notable_word:
    best_products_list_4.append(review)

#make a list of the top few products with the most amount of notable words from the users review and make another list containing the number of notable words in each of the top reviews

top_products = []
word_amounts = []
for review in best_products_list_4:
 __x__ = review
 __y__ = json.loads(__x__)
 review_text_5 = __y__["reviewText"]
 review_text_5 = review_text_5.split()
 word_counter = 0
 for word in review_text_5:
  for notable_word in most_notable_words_fixed:
   if word == notable_word:
    word_counter = word_counter + 1
 if word_counter >= 3:
  top_products.append(__y__["asin"])
  word_amounts.append(word_counter)

#fix if necessary
top_products_fixed = []
for asin in top_products:
    if asin not in top_products_fixed:
        top_products_fixed.append(asin)

#fix if necessary
word_amounts_fixed = []
for amount in word_amounts:
 if amount not in word_amounts_fixed:
  word_amounts_fixed.append(amount)

print('OTHER PRODUCT USER IS MOST LIKELY TO BUY:')
print(top_products_fixed[-1])
#assign x and y values
#x = top products
#y = number of times a notable word appeard
x = top_products_fixed
y = word_amounts_fixed
fig2 = plt.figure(figsize=(6, 5)) 

# graph labels
plt.title("product recommendations that match the selected user's criteria (all five star products)")
plt.xlabel("product asin number")
plt.ylabel("number of similar words")

plt.bar(x,y)
# shows the graph
plt.show()

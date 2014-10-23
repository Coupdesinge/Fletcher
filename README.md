Fletcher
========

PROJECT SPEC

1.Audience:
Yelp readers who want more context for the reviews they are reading about a particular business, and those who
ask themselves how much weight they should give a certain review given they don't know much about the yelper who 
wrote it. I.e., is this super negative review worth my attention, or does this Yelper care more about 
a restaurant's feng shui then I would?

2.Central Question:
Can we give more precise meaning to the star ratings on Yelp? 

3.Question Breakdown:
-If Yelper X gave their restaurant experience Y stars, can we use information from their full corpus 
of reviews and related ratings to better define what Y stars means to them?
-What sorts of businesses does Yelper X review and are there any biases in their reviews for particular kinds of businesses?
-Is Yelper X an "expert" in any particular kind of business?
-What are the general review trends and biases across business types on Yelp? E.g., do restaurants tend to have more variation in 
positive and negative reviews than, say, pet spas?

4.Data:
-I will be using the Yelp academic dataset, which I painstakingly downloaded from http://www.yelp.com/dataset_challenge
-252,898 users, 1,125,458 reviews and 42,153 businesses.
-The data came organized by business, reviews and user. I will store these in a mongo db 

5.Analysis:
-using the set of reviews available per user, discover the sub-topics within each star rating using unsupervised cluster
analysis. Both generally and then according to business type.
-measure of typicality of review for the yelper?
-measure of typicality of review for the business?

6.Deliverable:
-a short blog post describing this project
-Yelp reviewer profiles already have small graphs displaying the distribution of their ratings and a pie chart of the kinds
of businesses they have reviewed. I want to add the information I get from the analysis to the star ratings they give the business
ON the business's Yelp page. I will create a sample yelp review page displaying a prototype of this new metric.

7.Challenges
-I don't know how many complete sets of reviews I have for each reviewer.
-I don't know if any of this means anything.


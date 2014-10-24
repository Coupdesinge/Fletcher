Fletcher
========

PROJECT SPEC

#1.Audience:
Yelp readers who want more context for the reviews they are reading about a particular business, and those who
ask themselves how much weight they should give a certain review given they don't know much about the yelper who 
wrote it. I.e., is this super negative review worth my attention, or does this Yelper care more about 
a restaurant's feng shui then I would?

#2.Central Question:
Can we give more precise meaning to the star ratings on Yelp? 

#3.Question Breakdown:
<br>--If Yelper X gave their restaurant experience Y stars, can we use information from their full corpus 
of reviews and related ratings to better define what Y stars means to them?
<br-->What sorts of businesses does Yelper X review and are there any biases in their reviews for particular kinds of businesses?
<br>--Is Yelper X an "expert" in any particular kind of business?
<br>--What are the general review trends and biases across business types on Yelp? E.g., do restaurants tend to have more variation in positive and negative reviews than, say, pet spas?

#4.Data:
<br>--I will be using the Yelp academic dataset, which I painstakingly downloaded from http://www.yelp.com/dataset_challenge
<br>--252,898 users, 1,125,458 reviews and 42,153 businesses.
<br>--The data came organized by business, reviews and user. I will store these in a mongo db 

#5.Analysis:
<br>--Will use the set of reviews available per user for a large set of users, discover the sub-topics within each star rating using unsupervised cluster analysis and some sort of dimension reduction. Haven't played with this yet.

#6.Deliverables:
<br>--a short blog post describing this project
<br>--Yelp reviewer profiles already have small graphs displaying the distribution of their ratings and a pie chart of the kinds
of businesses they have reviewed. I want to add the information I get from the analysis to the star ratings they give the business
ON the business's Yelp page. I will create a sample yelp review page displaying a prototype of this new metric.

#7.Challenges
<br>--I don't know how many complete sets of reviews I have for each reviewer.
<br>--I'm not sure if I am taking proper advantage of the size of my dataset when I'm just doing cluster analysis
on a per-user basis


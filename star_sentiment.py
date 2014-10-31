import pickle
from collections import defaultdict
from textblob import TextBlob
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from itertools import izip

###clean and put into 5 separate lists

##for each star list vectorize
##cluster based on size of vector
##put clusters in a list
##for each cluster get the tf-idf of the cluster
##pull the top 5 words
##get sentences with top 5 words
##take two sentences with highest polarity, and sentiment measure according to star rating
##return star rating and sentences

###GET ALL USER REVIEWS AND RETURN A LIST OF 5 LISTS OF REPRESENTATIVE SENTENCES FOR EACH RATING
###AS WELL AS AVERAGE POLARITY FOR TOP SENTENCES IN EACH RATING CLUSTER 

class GetReviews(object):
	'''get pickle file of a users reviews, clean and return as 5 lists of reviews per start rating'''
	#no_apostros = {"'": "","\'": "","\n": " ","&": "and"}
	
	def pickle_to_dict(self, pfile):
		''' take pickle and turn into a dictionary w star ratings as keys and lowercase, partially cleaned review strings as values'''
		with open(pfile, 'r') as picklefile:
		 	data = pickle.load(picklefile)

		user_dict = defaultdict(list)
		for d in data:
			user_dict[d['stars']].append(  ((d['text'].split('\n\nReturn Factor')[0]).lower()).replace('\n\n', ' ')  )
	
		return user_dict

	#def no_stopwords(self, review_list):
	#	'''takes a list of strings and returns a list without english stopwords'''
	#	return review_list
	
	def remove_apostrophes(self, s, no_apostros):
			apostros_re = re.compile('(%s)' % '|'.join(no_apostros.keys()))
			replace = lambda match: no_apostros[match.group(0)]	
			return apostros_re.sub(replace, s)

	def clean_reviews(self, user_dict):
		'''take extra elements out of review strings in dict, return dict'''
		no_apostros = {"'":"", "\'":"", "\n":" ", "&":"and"}
		
		for i in range(1,6):
			user_dict[i] = [self.remove_apostrophes(s, no_apostros) for s in user_dict[i]]
		return user_dict

	def get_reviews(self, pfile):
			
			return self.clean_reviews(self.pickle_to_dict(pfile))

class Cluster(object):
	'''takes a single list of strings, e.g the values of one key in the user_dict returned by get_reviews'''
	
	def vectorize(self, string_list):
		'''takes a list of strings and turns into a tfid vector'''
		vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,1))
		star_vectors = vectorizer.fit_transform(string_list)
		return star_vectors

	def vector_size(self, star_vectors):
		'''returns the number of rows in the vector'''
		return star_vectors.shape[0]
	
	def kmeans_cluster(self, star_vectors, string_list):
		'''returns dict of clusters, reviews, with num clusters  based on size of vector'''
		s = self.vector_size(star_vectors)
		if(s <= 20):
			km = KMeans(n_clusters=2)
		elif(s <= 100):
			km = KMeans(n_clusters=4)
		else:
			km = KMeans()

		km_fit = km.fit(star_vectors)
		clusters = km_fit.predict(star_vectors)
		
		'''create dict of reviews with clusters as keys'''
		reviews = defaultdict(list)
		for i in range(0, len(string_list)):
			reviews[clusters[i]].append(string_list[i])
		
		return reviews

	def tfidf_on_clusters(self, cluster_dict):
		'''take clusters dict and return new dict with clusters as keys and values containing 5 words with highest tfidf for each cluster'''
		vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,1))
		dict_to_list = [' '.join(cluster_dict[i]) for i in cluster_dict.keys()]
	
		v = vectorizer.fit_transform(dict_to_list)  #vectorize the list of clusters
		
		tfidf_lists = defaultdict(list)
		for i in range(len(dict_to_list)):
				words = v[i].data.argsort()[-5:]
				for j in v[i].indices[words]:
						tfidf_lists[i].append(vectorizer.get_feature_names()[j])
		
		return tfidf_lists

	def tfidf_sentences(self, cluster_dict, tfidf_dict):
		'''take a cluster dict and top tfidf dict and return a dict with (sentence, polarity, subjectivity) tuples'''
		top_sentences = defaultdict(list)
		for (c, t) in izip(cluster_dict.keys(), tfidf_dict.keys()):
				sents = []
				for i in cluster_dict[c]:
						for s in TextBlob(i).sentences:
								sents.append(s)
				for s in sents:
						for w in tfidf_dict[t]:
								if w in s:
										f = s.sentiment
										top_sentences[c].append((s, f.polarity, f.subjectivity))
										break
		return top_sentences


	def greatest_polarity(self, top_sentences):
		'''take a dict of sentence sentiment tuples for each cluster and return a LIST containing the 'best' two sentences of each cluster'''
		for s in [top_sentences[c] for  c in top_sentences.keys()]:
			
	def test_cluster (self, reviews_dict):
		'''take list of strings and return dict and return a list of top sentences, sentiment tuples, sans subjectivity'''
		star_vectors = self.vectorize(reviews_dict[1])
		new_dict = self.kmeans_cluster(star_vectors, reviews_dict[1])
		tfidfs = self.tfidf_on_clusters(new_dict)
		sentences = self.tfidf_sentences(new_dict, tfidfs)
		return sentences


class GetSentences(Cluster):
		'''
		generate a reviews dict from a pickle file of all of a users reviews
		for each star rating, return a list of 'best' two sentences and sentiments
		calculate the average positive and negative polarities per star rating -- return these in a list
		'''
		
		def get_average_polarities(reviews_dict):
				'''takes a dict of reviews, sentiment tuples and returns a list of average polarities per rating'''
				polarity_list = [['One Star',one_pos], ['One Star', one_neg], ['Two Stars', two_pos], ['Two Stars', two_neg], ['Three Stars',three_pos
								],['Three Stars',three_neg], ['Four Stars',four_pos] ,['Four Stars',four_neg],['Five Stars', five_pos],['Five Stars', five_neg]]
				return polarity_list

		def get top_sentences(reviews_dict):
				'''takes a reviews dict and returns a list of top sentences per rating'''

		def get_user_sentences(picklefile):

				reviews_dict=self.get_reviews(picklefile)
				
				##for value in review_dict, get the sentences from the value
					##split the polarities in to positive and negative 
					##RETURN  the average polarity list
					##RETURN  the top sentences

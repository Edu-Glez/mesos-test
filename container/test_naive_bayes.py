import pickle
import pandas as pd
#import numpy as np
import nltk
import time
start_time = time.time()

a=pd.read_table('tweets_pos_clean.txt')
b=pd.read_table('tweets_neg_clean.txt')


aux1=[]
aux2=[]
auxiliar1=[]
auxiliar2=[]
for element in a['Text']:
	for w in element.split():
		if (w==':)' or len(w)>3):
			auxiliar1.append(w)
	aux1.append((auxiliar1,'positive'))
	auxiliar1=[]

for element in b['text']:
	for w in element.split():
		if (w==':(' or len(w)>3):
			auxiliar2.append(w)
	aux2.append((auxiliar2,'negative'))
	auxiliar2=[]

aux1=aux1[:10000]
aux2=aux2[:20000]

pos_df=pd.DataFrame(aux1)
neg_df=pd.DataFrame(aux2)

pos_df.columns=['words','sentiment']
neg_df.columns=['words','sentiment']

#table_aux=[pos_df,neg_df]
#tweets1=pd.concat(table_aux)
#tweets1.columns('words','sentiment')
table_aux1=aux1+aux2

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

word_features = get_word_features(get_words_in_tweets(table_aux1))

training_set = nltk.classify.apply_features(extract_features, table_aux1)
classifier = nltk.NaiveBayesClassifier.train(training_set)

word_features = list(word_features)

with open('objs2.pickle','wb') as f:
	pickle.dump([classifier, word_features],f)

print("Tomo %s segundos ejecutarse" % (time.time() - start_time))

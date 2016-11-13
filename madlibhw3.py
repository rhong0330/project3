# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random


from nltk.book import *


print(text2[:150])
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB" : "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "RB":.1}

tagged_tokens = nltk.pos_tag(text2[:150])
def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word
final_words = []
for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))
print ("".join(final_words))


#
# print(text1)
# print(text2)
# print("\n\n")
# print("Length of ",text1,"is",len(text1))
# print("Length of ",text2,"is",len(text2))
# print("Unique tokens in",text1," are: ",len(set(text1)))
# print("Unique tokens in",text2,"are: ",len(set(text2)))
# print("\n\nList of unique words")
# print(sorted(set(text2))[:15])
# print(sorted(set(text2),reverse=True)[:15])
# print("\n\nFrequency Distribution")
# #Frequency Distribution
# fdist1 = FreqDist(text1)
# print(fdist1)
# print(fdist1.most_common(25))
# print("\n\nWords with more characters")
# #How about "long" words
# long_words = [w for w in text1 if len(w)>15]
# print(long_words)
# print("\n\nBigrams")
# print(list(bigrams(text4))[:20]) #text8 would get me in trouble
# print("\n\nCollocations")
# print(text4.collocations())



#
# from nltk import word_tokenize,sent_tokenize
# text = "Hello students, how are you doing today? Have you recovered from the exam?  I hope you are feeling better.  Things will be fine."
# print(sent_tokenize(text))
# print(word_tokenize(text))
# for i in word_tokenize(text):
# 	print(i)

#
# debug = False #True
#
# # get file from user to make mad lib out of
# if debug:
# 	print ("Getting information from file madlib_test.txt...\n")
# fname = "madlibtest2.txt" # need a file with this name in directory
#
# f = open(fname, 'r')
# para = f.read()
# tokens = nltk.word_tokenize(para)
# print("TOKENS")
# print(tokens)
# tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:5]:
# 		print (tup)

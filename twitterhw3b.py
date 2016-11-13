import tweepy
from textblob import TextBlob

from nltk.corpus import subjectivity
#auth info
access_token = "793163334703079424-8ZmEgNDlr6UsRRDagzyzarR4C2rt2op"
access_token_secret = "Naq5zzb5R6ySS8VLCtxR4YMAlrZkxuAEld37eJOpYNFip"
consumer_key = "vYhgzFXdLu5WMXMNQtZaWBx4D"
consumer_secret = "CwTs5IKgxuhObbFd8ylko6vSl0uXq3lsJ5PIkSHbtMLXA13P08"

#authenticating
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#change this string to search other terms
search_term = "trump"

#search
public_tweets = api.search(search_term)


subj = 0 #total subj
pol = 0 #total pol
count = 0 #total count

#print each tweet
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text) #analyze tweet
	subj += analysis.sentiment.subjectivity #accum subj
	pol += analysis.sentiment.polarity #accum pol
	count += 1 #accum count

print("\nAverage subjectivity of the results: " + str(subj/count))
print("Average polarity of the results: " + str(pol/count))
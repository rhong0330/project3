import tweepy

#auth info
access_token = "793163334703079424-8ZmEgNDlr6UsRRDagzyzarR4C2rt2op"
access_token_secret = "Naq5zzb5R6ySS8VLCtxR4YMAlrZkxuAEld37eJOpYNFip"
consumer_key = "vYhgzFXdLu5WMXMNQtZaWBx4D"
consumer_secret = "CwTs5IKgxuhObbFd8ylko6vSl0uXq3lsJ5PIkSHbtMLXA13P08"

#authenticating
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#filename of jpg
#change the name to upload different local files
str_jpgfile = "twitter3a.jpg"

#updating profile image & posting
api.update_with_media(str_jpgfile,"#UMSI-206 #Proj3")
api.update_profile_image(str_jpgfile)

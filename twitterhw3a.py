import tweepy
from PIL import Image
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

jpgfile = Image.open("twitter3a.jpg")
#pic = StringIO('twitter3a.jpg', jpgfile)

access_token = "793163334703079424-8ZmEgNDlr6UsRRDagzyzarR4C2rt2op"
access_token_secret = "Naq5zzb5R6ySS8VLCtxR4YMAlrZkxuAEld37eJOpYNFip"
consumer_key = "vYhgzFXdLu5WMXMNQtZaWBx4D"
consumer_secret = "CwTs5IKgxuhObbFd8ylko6vSl0uXq3lsJ5PIkSHbtMLXA13P08"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
print(api.verify_credentials())
api.update_with_media("twitter3a.jpg","#UMSI-206 #Proj3")
api.update_profile_image("twitter3a.jpg")

import tweepy
import time
import datetime

ACCESS_TOKEN = '1107660530746097665-4A08UMu4NZY5bYRFDgm9jXy16HxUZk'
ACCESS_SECRET = 'MBNVgVtbwy3Imm6bnCUIFhugyDM6qz8c4hLY8tNMBVzqx'
CONSUMER_KEY = '8UXMQtk8z3W0L6O7ySzpvlb9L'
CONSUMER_SECRET = 'BK8zJCFyekpnahIIuqtsGVzruWFTZ4fRFMKzmuubRd7okigOzw'
SEARCH=input("Enter the search string: ")
FROM=str("2016-01-01")
TO=str("2019-01-01")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string: "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

i=0

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, screen_name='@CharlotteMag', q=SEARCH, rpp=100, count=20, result_type="recent", include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write(" ")
	f.write('^"')
	f.write(res.text.replace('\n',''))
	f.write('^"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ",i)
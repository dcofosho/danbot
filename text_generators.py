def hello_twitter(num):
	tweet = "hello twitter! This is tweet number %s \n" % (num, )
	return tweet

from nytimesarticle import articleAPI
import datetime, credentials
from dateutil.relativedelta import relativedelta
from random import randint

api=articleAPI(credentials.nytkey)

def x_years_ago(x):
	return (datetime.datetime.now() - relativedelta(years=x)).strftime('%Y%m%d')

def get_nyt_tweet():
	counter=1
	while True:
		try:
			numYearsAgo = randint(2, 150)
			target_date=int(x_years_ago(numYearsAgo))
			print('begin date equals %s'%str(target_date))
			articles = api.search(q="Brooklyn", begin_date=target_date, end_date=target_date)
			tweet = 'On this day in Brooklyn history, %s years ago: %s'%(str(numYearsAgo), articles['response']['docs'][0]['web_url'],)
			print(tweet)
			return tweet
		except:
			print('Failed %s times'%str(counter))
			counter += 1
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
# importing the csv module
import csv
import datetime
import json
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken="-"
asecret=""

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        username = all_data["user"]["screen_name"]

        date = all_data["created_at"]

        followers = all_data["user"]["followers_count"]
        
        if all_data["user"]["verified"]:
            verified = 'Yes'
        else:
            verified = 'No'

        retweet = all_data["retweet_count"]

        name = all_data["user"]["name"]

        tweet_url = 'https://twitter.com/'+all_data["user"]["screen_name"]+'/status/'+str(all_data["id"])

        sent = analyser.polarity_scores(tweet)
        if (sent["neg"]>sent["pos"]):
            sentiment = "Negative"
        elif (sent["neu"]>sent["pos"]):
            sentiment = "Neutral"
        else:
            sentiment = "Positive"

        sentiment_score = sent["compound"]
        # field names
        fields = ['Date','Name', 'Username', 'Tweet', 'Followers', 'Verified', 'URL', 'Retweets', 'Sentiment', 'Sentiment Score']
        
        # data rows of csv file
        rows = [ [date, name, username, tweet, followers, verified,tweet_url, retweet, sentiment, sentiment_score]]
        
        # name of csv file
        filename = datetime.datetime.now().strftime("%Y-%m-%d")+".csv"
        
        
        # writing to csv file
        with open(filename, 'a+') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            
            # writing the fields
            if not(os.path.exists(filename) and os.path.getsize(filename) > 0):
                csvwriter.writerow(fields)
            
            # writing the data rows
            csvwriter.writerows(rows)

        print((date,username,tweet, followers,))
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
#Enter Your keywords here
keywords = ["github","microsoft"]

twitterStream = Stream(auth, listener())
twitterStream.filter(track=keywords)
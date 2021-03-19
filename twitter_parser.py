# Uses the twitter API in order to search for twitters with a particular hashtag in a particular location. It allows you
# to search for a specific number of tweets if you are rate limited by the twitter API.

import datetime
import time
import tweepy

consumer_key = "*****"
consumer_secret = "*****"
access_token = "*****"
access_token_secret = "*****"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def tweets_to_text_file(num_tweets):
    while True:
        # Initialise the final piece of text as an empty string
        final_text = ""
        # For every tweet that is found within our search criteria
        for tweet in tweepy.Cursor(api.search, q='#hongkong', geocode='22.276960,114.135010,16mi', tweet_mode="extended").items(
                num_tweets):

            print("NEW TWEET: " + tweet.full_text)
            # Add the tweet to our final piece of text
            final_text += tweet.full_text

        # Now that we have all of the tweets saved inside final_text, this writes it to a text file with the
        # name as tweets_year month day.txt  e.g. tweets_20191201.txt for the 01/12/2019
        # This is done so a unique text file name is generated each day
        with open("tweets_" + datetime.datetime.now().strftime("%Y%m%d") + ".txt", "w") as text_file:
            text_file.write(final_text)

        # Sleeps for 24 hours, so if the program is left to run, it would keep on querying twitter once a day
        print("Sleeping for 24 hours")
        time.sleep(86400)


# Will save all of the tweets for each day as a seperate text file
tweets_to_text_file(num_tweets=1000)


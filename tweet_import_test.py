import tweepy
import db_manager


#account 1
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#establish connection to twitter API
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#Error handling
if (not api):
    print ("Problem connecting to API")


#List information
slug = 'SafeRoad'
owner = 'c14400718'

#get db manager
db = db_manager.db_manager()


def getFirstTweet():
    print("First tweets")
    tweets = api.list_timeline(owner_screen_name=owner, slug=slug, include_rts=False, count=10)
    if (len(list(tweets)) > 0):
        for tweet in tweets:
            print("First")
            db.db_insert(tweet)
            return
    else:
        print("No New Tweets")
        more_tweets = False
        return more_tweets

def getTweetNew(limit, more_tweets):
    tweets = api.list_timeline(owner_screen_name=owner, slug=slug, since_id=limit, include_rts=False, count=10)
    if (len(list(tweets)) > 0):
        for tweet in tweets:
            db.db_insert(tweet)
            print("new")
    else:
        print("No New Tweets")
        more_tweets = False
        return more_tweets

def getTweetOld(limit):
    tweets = api.list_timeline(owner_screen_name=owner, slug=slug, max_id=limit, include_rts=False, count=10)
    if (len(list(tweets)) > 0):
        for tweet in tweets:
            db.db_insert(tweet)
            print("old")
        return True
    else:
        print("No Old Tweets")
        more_tweets = False
        return more_tweets




def main():
    i = 0
    new_tweets = True

    try:
        while(new_tweets):
                tweet_max = db.get_tweet_max()
                if (tweet_max is None):
                    new_tweets = getFirstTweet()

                else:
                    new_tweets = getTweetNew(tweet_max, new_tweets)
                i = i + 1

        old_tweets = True
        while(old_tweets):
            db_min = db.get_tweet_min()
            old_tweets = getTweetOld(db_min)
            i = i + 1


        print("Cannot get any more Tweets")



    except tweepy.TweepError as e:
        print("some error: " + str(e))
        print("Downloaded " + str(i) + " tweets.")


if __name__ == '__main__':
    main()

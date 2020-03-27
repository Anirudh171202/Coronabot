import GetOldTweets3 as got

def dumps(lst):
    print("[")
    for i in lst:
        print(f"  {str(i[0]), i[1]},")
    print("]")

username = 'WHO IS COVID'
count = 10 # Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                        .setMaxTweets(count)

print("Ani")
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria) # Creating list of chosen tweet data
print("Vishnu Anand")
user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

print(dumps(user_tweets))
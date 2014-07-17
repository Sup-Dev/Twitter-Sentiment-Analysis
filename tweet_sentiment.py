import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def tweet_score(fp, tp):
    afinnfile = open(fp)
    tweet_file = open(tp)
    scores = {}
    tweets = []

    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)

    for tweet in tweet_file:
        parse_tweet = json.loads(tweet, 'utf-8')
        if ('text' in parse_tweet):
            tweets.append(parse_tweet[u'text'])

    for tweet in tweets:
        sentiment_value = 0
        for word in scores.keys():
            sentiment_value += (tweet.encode('utf-8').count(word)*scores[word])
        print(sentiment_value)

    # print tweets
    # print scores.items()

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    tweet_score(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()

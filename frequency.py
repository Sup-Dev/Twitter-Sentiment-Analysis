import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    tweets = []
    terms = {}
    total = 0

    for tweet in tweet_file:
        parse_tweet = json.loads(tweet, 'utf-8')
        if ('text' in parse_tweet):
            tweets.append(parse_tweet[u'text'])

    for tweet in tweets:
        words = tweet.encode('utf-8').split()
        total += len(words)

        for word in words:
            if word not in terms.keys():
                terms[word] = 1
            else:
                terms[word] += 1

    for k,v in terms.items():
        print k + " " + str(float(v)/total)


if __name__ == '__main__':
    main()

import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    new_scores = {}
    tweets = []

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for tweet in tweet_file:
        parse_tweet = json.loads(tweet, 'utf-8')
        if ('text' in parse_tweet):
            tweets.append(parse_tweet[u'text'])

    for tweet in tweets:
        new_words = tweet.encode('utf-8').split()
        sentiment_value = 0
        for word in scores.keys():
            sentiment_value += (tweet.encode('utf-8').count(word)*scores[word])
        for new_word in new_words:
            if sentiment_value > 0:
                if new_word not in new_scores.keys():
                    new_scores[new_word] = [0,1,1]
                else:
                    new_scores[new_word][1] += 1
                    new_scores[new_word][2] += 1
            elif sentiment_value < 0:
                if new_word not in new_scores.keys():
                    new_scores[new_word] = [1,0,1]
                else:
                    new_scores[new_word][0] += 1
                    new_scores[new_word][2] += 1
            else:
                if new_word not in new_scores.keys():
                    new_scores[new_word] = [0,0,1]
                else:
                    new_scores[new_word][2] += 1

    senti_scores = {}

    for word in new_scores.keys():
        v = new_scores[word]

        if v[0] != 0:
            senti_scores[word] = ((v[1]/float(v[2]))/(v[0]/float(v[2])))
        else:
            senti_scores[word] = (v[1]/float(v[2]))

        print word + " " + str(senti_scores[word])


if __name__ == '__main__':
    main()

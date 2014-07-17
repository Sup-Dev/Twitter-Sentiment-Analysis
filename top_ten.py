import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    tags = {}

    for tweet in tweet_file:
        parse_tweet = json.loads(tweet, 'utf-8')
        if ('entities' in parse_tweet):
            entities = parse_tweet[u'entities']
            if 'hashtags' in entities:
                hashtags = entities['hashtags']

                for tag in hashtags:
                    tag_text = tag['text']

                    if tag_text not in tags.keys():
                        tags[tag_text] = 1
                    else:
                        tags[tag_text] += 1

    for i in range(10):
        max_tag = max(tags.values())
        for tag in tags.keys():
            if tags[tag] == max_tag:
                print tag + " " + str(max_tag)
                tags[tag] = -1
                break



if __name__ == '__main__':
    main()
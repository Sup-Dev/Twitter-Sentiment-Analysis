import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }

    scores = {}
    state_scores = {}
    state_sentiment = {}
    tweets = []

    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for tweet in tweet_file:
        parse_tweet = json.loads(tweet, 'utf-8')
        if 'place' in parse_tweet:
            place = parse_tweet['place']
            if place != None and 'country_code' in place:
                if place['country_code'] == 'US':
                    if 'full_name' in place:
                        temp_state = place['full_name'].split(',')
                        if temp_state[1][1:] in states.keys():
                            state = states[temp_state[1][1:]]

                            if 'text' in parse_tweet:
                                tweets.append((state, parse_tweet[u'text']))

                        elif temp_state[0] in states.values():
                            state = temp_state[0]

                            if 'text' in parse_tweet:
                                tweets.append((state, parse_tweet[u'text']))


    for tweet_tuple in tweets:
        tweet = tweet_tuple[1]
        sentiment_value = 0

        for word in scores.keys():
            sentiment_value += (tweet.encode('utf-8').count(word)*scores[word])

        if tweet_tuple[0] not in state_scores.keys():
            state_scores[tweet_tuple[0]] = [sentiment_value, 1]
        else:
            state_scores[tweet_tuple[0]][0] += sentiment_value
            state_scores[tweet_tuple[0]][1] += 1

    for state in state_scores.keys():
        state_sentiment[[k for k, v in states.iteritems() if v == state][0]] = float(state_scores[state][0])/state_scores[state][1]

    happiest = max(state_sentiment.values())

    for state in state_sentiment.keys():
        if state_sentiment[state] == happiest:
            print state
            break


if __name__ == '__main__':
    main()
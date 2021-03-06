## Sentiment Analysis on Live Twitter Stream using Python
=========================================================

### Python Version -- Python 2.7.x

The descriptions on each file is below:

### apikey.py

Imports the collects the keys from the text file **Twitter API.txt**. The list of keys in order is as follows:

1. api_key
2. api_secret
3. access_token_key
4. access_token_secret

### twitterstream.py

Outputs the live Twitter stream on your shell. This file requires the module **oauth2** to work.

Use the following command in your terminal to install **oauth2**:

```
$ pip install oauth2
```

To get an output of your Twitter stream to a file use the following command:

```
$ python twitterstream.py > output.txt
```

### tweet_sentiment.py

Derives the sentiment of each tweet. This file will compute the sentiment of each tweet based on the sentiment scores. The sentiment of a tweet is calculated by adding the sentiment of each word in the tweet.
To calculate the sentiments of tweets generated, use the following command:

```
$ python tweet_sentiment.py AFINN-111.txt output.txt
```

The **AFINN-111.txt** file contains a list of pre-computed sentiment scores.

### term_sentiment.py

Derives the sentiment of new terms. Sentiment scores of new terms is calculated using the formula:

```
 p(Positive Word/Topic Word)/p(Negative Word/Topic Word)
```

Calculate new sentiment scores using the following command:

```
$ python term_sentiment.py AFINN-111.txt output.txt
```

### frequency.py

Computes the *term frequency histogram* of the Tweeter stream. The frequency is calculated using the formula:

 ```
 [Number of occurrences of the term in all tweets]/[Number of occurrences of all terms in all tweets]
 ```

Run the following command to compute the frequencies:

```
$ python frequency.py output.txt
```

### happiest_state.py

Computes and returns the name of the happiest state in US.

Type the following command on your terminal:

```
$ python happiest_state.py AFINN-111.txt output.txt
```

### top_ten.py

Computes the ten most frequently used hashtags for the data gathered from the Tweeter stream.

```
$ python top_ten.py output.txt
```

### AFINN-111.txt

Contains a list of precomputed sentiment scores.

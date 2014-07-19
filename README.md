# Sentiment Analysis on Live Twitter Stream using Python

## Python Version -- Python 2.7.x

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

Derives the sentiment of each tweet. This file will compute the sentiment of each tweet based on the sentiment scores.

import os

def twitter_apikeys():
    key_file_dir = os.path.dirname(os.path.dirname(__file__))
    key_file = open(os.path.join(key_file_dir, 'Twitter API.txt'))
    key_list = []

    for key in key_file:
        key_list.append(key[:-1])

    return key_list

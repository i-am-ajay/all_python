__author__ = 'gaa8664'

import oauth2
import constants
from urllib import parse as parseurl

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)
client = oauth2.Client(consumer)

response, content =  client.request(constants.REQUEST_TOKEN_URL, method = 'POST')
if response.status != 200:
    print("Not ok")
auth_token = dict(parseurl.parse_qsl(content.decode('utf8')))
print(constants.ACCESS_TOKEN_URL+'?oauth_token='+auth_token['oauth_token'])

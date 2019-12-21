from requests_oauthlib import OAuth1
import requests

# Create the auth
auth = OAuth1('API key',
              'API secret key',
              'Access token',
              'Access token secret', )

# Send the request with the auth
r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json', auth = auth)

# Print the returned data, simple!
print(r.content)

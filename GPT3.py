import openai
from datetime import datetime, timedelta
import tweepy
import time

while True: 
    apiKey = ''
    apikeySecret = ''

    accessToken = ''
    accessTokenSecret = ''

    oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
    oauth.set_access_token(accessToken, accessTokenSecret)
    openai.api_key = ""

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Write a Funny Tweet on technology",
        temperature=0.9,
        max_tokens=100,

    )
    tweet = response.choices[0]["text"]
    api = tweepy.API(oauth)
    result = api.update_status(status = tweet )
    print("Successful: ",datetime.now().strftime("%H:%M:%S")," ",tweet)
    time.sleep(7200)
    

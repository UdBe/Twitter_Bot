import requests
import tweepy
import time
from datetime import datetime, timedelta


def GetNews():

    apiKey = ''
    apikeySecret = ''

    accessToken = ''
    accessTokenSecret = ''

    oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
    oauth.set_access_token(accessToken, accessTokenSecret)

    query_params = {
        "source": "engadget",
        "sortBy": "top",
        "category": "technology",
        "apiKey": "",
        "from": datetime.today() - timedelta(days=1)

    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_page = res.json()

    article = open_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])


            tweet = (results[i]).rsplit("|")[0]
            api = tweepy.API(oauth)
            result = api.update_status(status = tweet )
            print("Successful: ",datetime.now().strftime("%H:%M:%S")," ",tweet)
            time.sleep(7200)


    GetNews()



if __name__ == '__main__':
    GetNews()

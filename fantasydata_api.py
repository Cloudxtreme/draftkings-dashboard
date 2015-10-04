# Fantasy Data API Functions

import json
import requests0 as requests
import arrow
from _keys import SUBSCRIPTION_KEY

BASE_URL = 'https://api.fantasydata.net/nfl/v2/JSON/'


# Fetch a list of fantasy player IDs by a list of names
def fetch_daily_fantasy_scoring(date):

    url = BASE_URL + 'DailyFantasyPoints/{}'.format(date)

    response = requests.get(
        url,
        headers={
            'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
            'Content-Type': 'application/json'
        }
    )

    fantasy_scores = response.json

    return fantasy_scores

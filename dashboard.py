from fantasydata_api import fetch_daily_fantasy_scoring
import arrow
from lineup import LINEUP

now = arrow.utcnow()
today = now.format('YYYY-MM-DD')

fantasy_scores = fetch_daily_fantasy_scoring(date=today)

for player_name in LINEUP:

    for score in fantasy_scores:
        if score['Name'] == player_name:
            print player_name, score['FantasyPoints']

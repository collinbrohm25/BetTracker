"""Module for contacting SportsDataIO for API data."""
import requests
import json
import logging


class Loader:
    def load(self):
        url = 'https://api.sportsdata.io/v3/nfl/stats/json/PlayerGameStatsByWeek/2024REG/8?key=9589ab58f6d642669d142c926287bb71'
        logging.info(f'Attempting to load data from: {url}')
        response = requests.get(url=url)
        if response.status_code == 200:
            logging.info('Loading sucessful!')
            load_response = []
            load_response = json.loads(response)
            return load_response

    
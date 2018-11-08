import requests
import json
import os


class SlackPager:


    def __init__(self, message):
        self.url = os.environ['SLACK_URL']
        self.headers = {
            'Content-type': 'application/json'
        }
        self.data = json.dumps({
            'text': message })


    def send_slack_pager_message(self):
        response = requests.post(
            self.url,
            headers=self.headers,
            data=self.data
        )

        if response.ok:
            return True
        else:
            return False
# - github.com/Vauth/aiuncensored - #

import requests
from typing import List, Dict
from googlesearch import get_random_user_agent

class AIUncensored:
    """
    Client = AIUncensored()
    Client.Chat(str, List[Dict[str, str]])
    """
    def __init__(self):
        self.version = 'v1.3'

        self.url = "https://darkai.foundation/chat"
        self.headers = {
            "User-Agent": (get_random_user_agent()).decode('utf-8'),
            "Accept": "text/event-stream",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": "https://www.aiuncensored.info/",
            "Content-Type": "application/json",
            "Origin": "https://www.aiuncensored.info",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "DNT": "1",
            "Sec-GPC": "1",
            "Priority": "u=1",
            "TE": "trailers"
        }
        self.model = "llama-3-70b"

    class OperationError(Exception):
        def __init__(self, error_text):
            self.error_text = error_text
            super().__init__(error_text)

    def Chat(self, query: str, history: List[Dict[str, str]]) -> str:
        json = {
            "query": query,
            "history": history,
            "model": self.model
        }
        response = requests.post(self.url, headers=self.headers, json=json)

        if response.text.startswith('event: error'):
            raise self.OperationError(eval(response.text.split('data: ')[-1])['data']['detail'])
        elif response.text.startswith('<!DOCTYPE html>'):
            raise self.OperationError('API URL does not seem to be valid anymore')
        elif response.text.startswith('data: '):
            return eval(response.text.split('data: ')[-1])['data']['message']
        else:
            raise self.OperationError("Wrong syntax detected, github.com/Vauth/aiuncensored.")

import requests

from FW.base_fw import BaseFW


class ApiBaseFw(BaseFW):

    def get_header(self):
        if self.manager.settings.access_token == '':
            self.manager.api_token.get_token()

        header = {
            'Content-Type': 'application/json',
            'Authorization': f'{self.manager.settings.token_type} {self.manager.settings.access_token}'
        }
        return header

    def request_get(self, url, params=None):
        response = requests.get(url, headers=self.get_header(), params=params)
        return response.json()

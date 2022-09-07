import requests as requests

from FW.API.api_base_fw import ApiBaseFw


class Token(ApiBaseFw):

    def get_token(self, user='test_user09'):

        url = f'{self.manager.settings.url_auth}/connect/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.manager.settings.users[user]['user_id'],
            'client_secret': self.manager.settings.users[user]['secret'],
        }

        response = requests.post(url, headers=headers, data=body, params=None)
        response = response.json()
        self.manager.settings.access_token = response['access_token']
        self.manager.settings.token_type = response['token_type']

        return response

import allure
import requests as requests

from FW.API.api_base_fw import ApiBaseFw


class Token(ApiBaseFw):

    @allure.step('Получение токена пользователя')
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

        self.request_log('POST', url, '', headers, body, response)
        return response

    @allure.step('Получение токена пользователя')
    def get_token_user_id_and_secret(self, user_id, secret):

        url = f'{self.manager.settings.url_auth}/connect/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': user_id,
            'client_secret': secret,
        }

        response = requests.post(url, headers=headers, data=body, params=None)
        response = response.json()
        self.manager.settings.access_token = response['access_token']
        self.manager.settings.token_type = response['token_type']

        self.request_log('POST', url, '', headers, body, response)
        return response

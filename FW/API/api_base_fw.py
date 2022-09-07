import allure
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

    @allure.step('request_get')
    def request_get(self, url, params=None):
        response = requests.get(url, headers=self.get_header(), params=params)
        return response.json()

    @allure.step('request_post')
    def request_post(self, url, body, params=None):
        response = requests.post(url, data=body, headers=self.get_header(), params=params)
        return response.json()

    @allure.step('request_put')
    def request_put(self, url, body, params=None):
        response = requests.put(url, data=body, headers=self.get_header(), params=params)
        return response.json()

    @allure.step('request_delete')
    def request_delete(self, url, params=None):
        response = requests.delete(url, headers=self.get_header(), params=params)
        return response.json()

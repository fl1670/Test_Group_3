import requests

from FW.API.api_base_fw import ApiBaseFw


class Users(ApiBaseFw):

    # Получение своего пользовательского профиля
    def get_users_profile(self, url, header):
        return requests.get(url, headers=header).json()



import requests as requests

from FW.API.api_base_fw import ApiBaseFw


class Token(ApiBaseFw):

    def get_token(self):

        url = 'https://auth-feature-development.gandiva.ru/connect/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': "5cd86e44-bb14-11ec-9437-0217dc7a50e7",
            'client_secret': "ZRxM+/Pc+sqZT6CBeeImgFbmlP14HImlL6HfB0uoDDbSmrEdtFQLmXJuV+yu6dBL",
        }

        response = requests.post(url, headers=headers, data=body, params=None)
        response = response.json()

        return response

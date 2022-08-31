from Tests.API.api_base import ApiBase


class TestToken(ApiBase):

    def test_get_token(self):

        response = self.APP.api_token.get_token()
        token = response['access_token']
        token_type = response['token_type']

        url = 'https://api-feature-development.gandiva.ru/api/Users/Profile'

        header = {
            'Content-Type': 'application/json',
            'Authorization': f'{token_type} {token}'
        }
        print(url)
        print(header)

        print(self.APP.api_users.get_users_profile(url, header))
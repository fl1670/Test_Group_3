import allure

from Tests.API.api_base import ApiBase


@allure.feature('Api')
@allure.story('Get token')
class TestToken(ApiBase):

    @allure.title('Получение токена (проверка access_token и token_type)')
    def test_get_token(self):
        token = self.APP.api_token.get_token()

        assert 'access_token' in token
        assert 'token_type' in token
        assert token['access_token'] != ''
        assert token['token_type'] != ''

    @allure.title('Получение токена для пользователя test_user09 и test_Boss01')
    def test_get_token_test_user9(self):
        self.APP.api_token.get_token('test_user09')
        user = self.APP.api_users.get_users_profile()
        assert user['login'] == 'testuser09'

        self.APP.api_token.get_token('test_Boss01')
        user = self.APP.api_users.get_users_profile()
        assert user['login'] == 'testboss01'

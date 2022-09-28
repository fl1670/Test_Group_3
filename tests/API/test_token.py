import allure
import pytest

from tests.API.api_base import ApiBase


@allure.epic('Api')
@allure.feature('Token')
@allure.story('Get token')
class TestToken(ApiBase):

    @allure.title('Получение токена (проверка access_token и token_type)')
    @pytest.mark.ApiTest
    @pytest.mark.Token
    def test_get_token(self):
        token = self.APP.api_token.get_token()

        assert 'access_token' in token
        assert 'token_type' in token
        assert token['access_token'] != ''
        assert token['token_type'] != ''

    data = [
        ('test_user09', 'testuser09'),
        ('test_Boss01', 'testboss01'),
        ('test_Boss02', 'testboss02'),
        ('test_Boss03', 'testboss03'),
        ('test_user09', 'qwertytyu'),
        ('test_user01', 'testuser01'),
        ('test_user02', 'testuser02'),
        ('test_user03', 'testuser03'),
        ('test_user04', 'testuser04'),
    ]

    @pytest.mark.ApiTest
    @pytest.mark.Token
    @allure.title('Получение токена для пользователя test_user09 и test_Boss01')
    @pytest.mark.parametrize("user_name, user_login", data)
    def test_get_token_parametrize(self, user_name, user_login):
        self.APP.api_token.get_token(user_name)
        user = self.APP.api_users.get_users_profile()
        assert user['login'] == user_login

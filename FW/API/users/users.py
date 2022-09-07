from FW.API.api_base_fw import ApiBaseFw


class Users(ApiBaseFw):

    # Получение своего пользовательского профиля
    def get_users_profile(self):
        return self.request_get(f'{self.manager.settings.url_api}/api/Users/Profile')




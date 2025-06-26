cookie_dict = self.session.cookies.get_dict()
cookie_dict['OCB_REMEMBER_2FA'] = self.username
cookie_dict['KEYCLOAK_REMEMBER_ME'] = "KEYCLOAK_REMEMBER_ME:{}".format(self.username)
self.session = self.get_new_session()
self.username = "AABBCCC"
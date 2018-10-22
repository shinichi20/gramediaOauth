"""
Milors OAuth2 backend : this system using for login to
    http://backend-gramedia.milors.stagingapps.net/admin/login
"""

from .oauth import BaseOAuth2

class MilorsOauth2(BaseOAuth2):
    name = 'milors'

    def get_user_id(self, details, response):
        user = response.get('user') or response.get('data') or {}
        return user.get('id')

    def get_user_details(self, response):
        user = response.get('user') or response.get('data') or {}
        username = user['username']
        email = user.get('email', '')
        fullname, first_name, last_name = self.get_user_names(
            user.get('full_name', '')
        )
        return {'username': username,
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name,
                'email': email}




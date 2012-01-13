"""
Tumblr OAuth support.
"""

from oauth.oauth import OAuthToken as Token
from oauth.oauth import OAuthRequest
from oauth.oauth import OAuthSignatureMethod_HMAC_SHA1 as SignatureMethod_HMAC_SHA1
from urllib import urlencode
from urllib import urlopen
from django.utils import simplejson
from social_auth.backends import ConsumerBasedOAuth
from social_auth.backends import OAuthBackend
from social_auth.backends import USERNAME

TUMBLR_SERVER = 'www.tumblr.com'
TUMBLR_AUTHORIZATION_URL = 'http://%s/oauth/authorize' % TUMBLR_SERVER
TUMBLR_REQUEST_TOKEN_URL = 'http://%s/oauth/request_token' % TUMBLR_SERVER
TUMBLR_ACCESS_TOKEN_URL = 'http://%s/oauth/access_token' % TUMBLR_SERVER
TUMBLR_CHECK_AUTH = 'http://api.tumblr.com/v2/user/info'


class TumblrBackend(OAuthBackend):
    name = 'tumblr'

    def get_user_id(self, details, response):
        return details[USERNAME]

    def get_user_details(self, response):
        user_info = response['response']['user']
        data = {
            USERNAME: user_info['name'],
            'email': '',
            'fullname': '',
            'first_name': '',
            'last_name': ''
        }

        return data


class TumblrAuth(ConsumerBasedOAuth):
    AUTHORIZATION_URL = TUMBLR_AUTHORIZATION_URL
    REQUEST_TOKEN_URL = TUMBLR_REQUEST_TOKEN_URL
    ACCESS_TOKEN_URL = TUMBLR_ACCESS_TOKEN_URL
    SERVER_URL = TUMBLR_SERVER
    SETTINGS_KEY_NAME = 'TUMBLR_CONSUMER_KEY'
    SETTINGS_SECRET_NAME = 'TUMBLR_CONSUMER_SECRET'
    AUTH_BACKEND = TumblrBackend

    def user_data(self, access_token):
        request = self.oauth_request(access_token, TUMBLR_CHECK_AUTH)
        json = self.fetch_response(request)
        try:
            return simplejson.loads(json)
        except ValueError:
            return None

    def unauthorized_token(self):
        request = self.oauth_request(token=None, url=self.REQUEST_TOKEN_URL)
        response = self.fetch_response(request)
        return Token.from_string(response)

    def oauth_request(self, token, url, extra_params=None):
        params = {'oauth_callback': self.redirect_uri}
        if extra_params:
            params.update(extra_params)

        if 'oauth_verifier' in self.data:
            params['oauth_verifier'] = self.data['oauth_verifier']

        request = OAuthRequest.from_consumer_and_token(
            self.consumer, token=token, http_url=url, parameters=params)
        request.sign_request(SignatureMethod_HMAC_SHA1(), self.consumer, token)

        return request

    def fetch_response(self, request):
        """Executes request and fetchs service response"""
        response = urlopen(request.to_url())
        return response.read()


BACKENDS = {
    'tumblr': TumblrAuth,
}

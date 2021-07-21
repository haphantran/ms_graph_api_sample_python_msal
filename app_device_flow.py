from msal import PublicClientApplication
import urllib
import json
import config
import logging
import sys


def api_endpoint(url):
    return urllib.parse.urljoin(f'{config.ROUSEURCE}/{CONFIG.api_version}/', url.lstrip(' /'))


def get_token(client_id=config.CLIENT_ID, authority_url=config.AUTHORITY_URL, scopes=config.SCOPES):

    app = PublicClientApplication(
        client_id=client_id,
        authority=authority_url
        # we are using username and password with Delegated permision -> don't need client secret
        # if you are using Application permision, use client_credential = config.CLIENT_SECRET
    )

    # token_response = app.acquire_token_by_username_password(
    #     config.USERNAME, config.PASSWORD, config.SCOPE
    # )

    flow = app.initiate_device_flow(scopes=scopes)
    print(flow["message"])

    result = app.acquire_token_by_device_flow(flow)

    token = result.get('access_token')

    print('sign in successfully') if token else print('error signing in')


if __name__ == '__main__':
    get_token()

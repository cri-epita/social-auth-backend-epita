"""
Epita OpenIdConnect:
"""
from social_core.backends.open_id_connect import OpenIdConnectAuth


class EpitaOpenIdConnect(OpenIdConnectAuth):
    name = 'epita'
    OIDC_ENDPOINT = 'https://accounts-beta.cri.epita.net/oidc'


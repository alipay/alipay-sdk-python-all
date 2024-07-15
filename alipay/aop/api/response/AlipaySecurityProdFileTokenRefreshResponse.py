#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RefreshWebofficeTokenResponse import RefreshWebofficeTokenResponse


class AlipaySecurityProdFileTokenRefreshResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdFileTokenRefreshResponse, self).__init__()
        self._refresh_weboffice_token_response = None

    @property
    def refresh_weboffice_token_response(self):
        return self._refresh_weboffice_token_response

    @refresh_weboffice_token_response.setter
    def refresh_weboffice_token_response(self, value):
        if isinstance(value, RefreshWebofficeTokenResponse):
            self._refresh_weboffice_token_response = value
        else:
            self._refresh_weboffice_token_response = RefreshWebofficeTokenResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdFileTokenRefreshResponse, self).parse_response_content(response_content)
        if 'refresh_weboffice_token_response' in response:
            self.refresh_weboffice_token_response = response['refresh_weboffice_token_response']

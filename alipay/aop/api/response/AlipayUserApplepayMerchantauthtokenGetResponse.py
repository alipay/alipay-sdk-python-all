#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiResponseHeader import OpenApiResponseHeader


class AlipayUserApplepayMerchantauthtokenGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserApplepayMerchantauthtokenGetResponse, self).__init__()
        self._merchant_auth_token = None
        self._response_header = None

    @property
    def merchant_auth_token(self):
        return self._merchant_auth_token

    @merchant_auth_token.setter
    def merchant_auth_token(self, value):
        self._merchant_auth_token = value
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, OpenApiResponseHeader):
            self._response_header = value
        else:
            self._response_header = OpenApiResponseHeader.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayUserApplepayMerchantauthtokenGetResponse, self).parse_response_content(response_content)
        if 'merchant_auth_token' in response:
            self.merchant_auth_token = response['merchant_auth_token']
        if 'response_header' in response:
            self.response_header = response['response_header']

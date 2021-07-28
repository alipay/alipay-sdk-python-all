#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BaseOpenApiResponseHeaderDTO import BaseOpenApiResponseHeaderDTO


class AlipayPayApplepayTransactionauthtokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayApplepayTransactionauthtokenCreateResponse, self).__init__()
        self._authentication_token = None
        self._response_header = None
        self._supports_settlement = None

    @property
    def authentication_token(self):
        return self._authentication_token

    @authentication_token.setter
    def authentication_token(self, value):
        self._authentication_token = value
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, BaseOpenApiResponseHeaderDTO):
            self._response_header = value
        else:
            self._response_header = BaseOpenApiResponseHeaderDTO.from_alipay_dict(value)
    @property
    def supports_settlement(self):
        return self._supports_settlement

    @supports_settlement.setter
    def supports_settlement(self, value):
        self._supports_settlement = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayApplepayTransactionauthtokenCreateResponse, self).parse_response_content(response_content)
        if 'authentication_token' in response:
            self.authentication_token = response['authentication_token']
        if 'response_header' in response:
            self.response_header = response['response_header']
        if 'supports_settlement' in response:
            self.supports_settlement = response['supports_settlement']

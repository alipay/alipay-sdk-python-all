#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BaseOpenApiResponseHeaderDTO import BaseOpenApiResponseHeaderDTO


class AlipayPayApplepayTransactionauthtokenDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayApplepayTransactionauthtokenDeleteResponse, self).__init__()
        self._response_header = None

    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, BaseOpenApiResponseHeaderDTO):
            self._response_header = value
        else:
            self._response_header = BaseOpenApiResponseHeaderDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayPayApplepayTransactionauthtokenDeleteResponse, self).parse_response_content(response_content)
        if 'response_header' in response:
            self.response_header = response['response_header']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class AlipaySecurityProdDesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdDesQueryResponse, self).__init__()
        self._dee = None
        self._string = None

    @property
    def dee(self):
        return self._dee

    @dee.setter
    def dee(self, value):
        if isinstance(value, GavintestNewLeveaOne):
            self._dee = value
        else:
            self._dee = GavintestNewLeveaOne.from_alipay_dict(value)
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdDesQueryResponse, self).parse_response_content(response_content)
        if 'dee' in response:
            self.dee = response['dee']
        if 'string' in response:
            self.string = response['string']

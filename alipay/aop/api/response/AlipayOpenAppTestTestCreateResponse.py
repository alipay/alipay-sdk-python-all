#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppTestTestCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppTestTestCreateResponse, self).__init__()
        self._province_code = None

    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppTestTestCreateResponse, self).parse_response_content(response_content)
        if 'province_code' in response:
            self.province_code = response['province_code']

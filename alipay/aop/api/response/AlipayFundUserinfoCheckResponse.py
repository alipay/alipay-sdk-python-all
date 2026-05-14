#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundUserinfoCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundUserinfoCheckResponse, self).__init__()
        self._is_pass = None

    @property
    def is_pass(self):
        return self._is_pass

    @is_pass.setter
    def is_pass(self, value):
        self._is_pass = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundUserinfoCheckResponse, self).parse_response_content(response_content)
        if 'is_pass' in response:
            self.is_pass = response['is_pass']

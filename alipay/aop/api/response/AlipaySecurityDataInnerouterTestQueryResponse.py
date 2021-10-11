#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityDataInnerouterTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataInnerouterTestQueryResponse, self).__init__()
        self._one = None

    @property
    def one(self):
        return self._one

    @one.setter
    def one(self, value):
        self._one = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataInnerouterTestQueryResponse, self).parse_response_content(response_content)
        if 'one' in response:
            self.one = response['one']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserIdenticalAuthbaseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserIdenticalAuthbaseQueryResponse, self).__init__()
        self._identical = None

    @property
    def identical(self):
        return self._identical

    @identical.setter
    def identical(self, value):
        self._identical = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserIdenticalAuthbaseQueryResponse, self).parse_response_content(response_content)
        if 'identical' in response:
            self.identical = response['identical']

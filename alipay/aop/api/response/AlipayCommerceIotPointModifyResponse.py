#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotPointModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotPointModifyResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotPointModifyResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']

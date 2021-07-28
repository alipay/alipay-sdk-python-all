#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceAntestAppversionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAntestAppversionQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                self._data.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAntestAppversionQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']

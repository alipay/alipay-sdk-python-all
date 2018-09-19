#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserUnicomDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserUnicomDataQueryResponse, self).__init__()
        self._data_balance = None

    @property
    def data_balance(self):
        return self._data_balance

    @data_balance.setter
    def data_balance(self, value):
        self._data_balance = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserUnicomDataQueryResponse, self).parse_response_content(response_content)
        if 'data_balance' in response:
            self.data_balance = response['data_balance']

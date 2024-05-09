#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseEntityroleHuaweimpQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseEntityroleHuaweimpQueryResponse, self).__init__()
        self._customer_name = None

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseEntityroleHuaweimpQueryResponse, self).parse_response_content(response_content)
        if 'customer_name' in response:
            self.customer_name = response['customer_name']

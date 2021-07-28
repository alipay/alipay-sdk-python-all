#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInspectSessionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInspectSessionQueryResponse, self).__init__()
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInspectSessionQueryResponse, self).parse_response_content(response_content)
        if 'value' in response:
            self.value = response['value']

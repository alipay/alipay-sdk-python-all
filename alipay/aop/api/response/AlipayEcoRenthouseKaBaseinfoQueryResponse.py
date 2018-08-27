#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRenthouseKaBaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRenthouseKaBaseinfoQueryResponse, self).__init__()
        self._ka_code = None
        self._ka_name = None
        self._valid = None

    @property
    def ka_code(self):
        return self._ka_code

    @ka_code.setter
    def ka_code(self, value):
        self._ka_code = value
    @property
    def ka_name(self):
        return self._ka_name

    @ka_name.setter
    def ka_name(self, value):
        self._ka_name = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRenthouseKaBaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'ka_code' in response:
            self.ka_code = response['ka_code']
        if 'ka_name' in response:
            self.ka_name = response['ka_name']
        if 'valid' in response:
            self.valid = response['valid']

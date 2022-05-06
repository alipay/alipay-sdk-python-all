#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdHaiguanNoauthCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdHaiguanNoauthCreateResponse, self).__init__()
        self._out_one = None
        self._out_three = None
        self._out_two = None

    @property
    def out_one(self):
        return self._out_one

    @out_one.setter
    def out_one(self, value):
        self._out_one = value
    @property
    def out_three(self):
        return self._out_three

    @out_three.setter
    def out_three(self, value):
        self._out_three = value
    @property
    def out_two(self):
        return self._out_two

    @out_two.setter
    def out_two(self, value):
        if isinstance(value, list):
            self._out_two = list()
            for i in value:
                self._out_two.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdHaiguanNoauthCreateResponse, self).parse_response_content(response_content)
        if 'out_one' in response:
            self.out_one = response['out_one']
        if 'out_three' in response:
            self.out_three = response['out_three']
        if 'out_two' in response:
            self.out_two = response['out_two']

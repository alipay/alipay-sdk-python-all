#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRentOrderSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderSignResponse, self).__init__()
        self._sign_launch_method = None
        self._sign_str = None

    @property
    def sign_launch_method(self):
        return self._sign_launch_method

    @sign_launch_method.setter
    def sign_launch_method(self, value):
        self._sign_launch_method = value
    @property
    def sign_str(self):
        return self._sign_str

    @sign_str.setter
    def sign_str(self, value):
        self._sign_str = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderSignResponse, self).parse_response_content(response_content)
        if 'sign_launch_method' in response:
            self.sign_launch_method = response['sign_launch_method']
        if 'sign_str' in response:
            self.sign_str = response['sign_str']

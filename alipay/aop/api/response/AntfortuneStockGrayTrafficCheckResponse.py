#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneStockGrayTrafficCheckResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockGrayTrafficCheckResponse, self).__init__()
        self._check_passed = None
        self._hit_message = None

    @property
    def check_passed(self):
        return self._check_passed

    @check_passed.setter
    def check_passed(self, value):
        self._check_passed = value
    @property
    def hit_message(self):
        return self._hit_message

    @hit_message.setter
    def hit_message(self, value):
        self._hit_message = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockGrayTrafficCheckResponse, self).parse_response_content(response_content)
        if 'check_passed' in response:
            self.check_passed = response['check_passed']
        if 'hit_message' in response:
            self.hit_message = response['hit_message']

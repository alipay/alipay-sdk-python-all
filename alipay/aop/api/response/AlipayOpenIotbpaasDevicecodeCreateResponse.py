#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotbpaasDevicecodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotbpaasDevicecodeCreateResponse, self).__init__()
        self._short_code = None

    @property
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, value):
        self._short_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotbpaasDevicecodeCreateResponse, self).parse_response_content(response_content)
        if 'short_code' in response:
            self.short_code = response['short_code']

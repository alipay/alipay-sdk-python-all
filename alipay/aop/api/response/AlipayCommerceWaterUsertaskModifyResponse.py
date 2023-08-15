#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWaterUsertaskModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWaterUsertaskModifyResponse, self).__init__()
        self._change_result = None
        self._change_type = None

    @property
    def change_result(self):
        return self._change_result

    @change_result.setter
    def change_result(self, value):
        self._change_result = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWaterUsertaskModifyResponse, self).parse_response_content(response_content)
        if 'change_result' in response:
            self.change_result = response['change_result']
        if 'change_type' in response:
            self.change_type = response['change_type']

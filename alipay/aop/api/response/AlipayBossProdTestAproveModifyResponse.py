#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdTestAproveModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdTestAproveModifyResponse, self).__init__()
        self._out_string = None

    @property
    def out_string(self):
        return self._out_string

    @out_string.setter
    def out_string(self, value):
        self._out_string = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdTestAproveModifyResponse, self).parse_response_content(response_content)
        if 'out_string' in response:
            self.out_string = response['out_string']

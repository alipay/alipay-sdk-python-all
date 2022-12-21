#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniBaseinfoNameCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBaseinfoNameCheckResponse, self).__init__()
        self._check_code = None
        self._check_memo = None

    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
    @property
    def check_memo(self):
        return self._check_memo

    @check_memo.setter
    def check_memo(self, value):
        self._check_memo = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBaseinfoNameCheckResponse, self).parse_response_content(response_content)
        if 'check_code' in response:
            self.check_code = response['check_code']
        if 'check_memo' in response:
            self.check_memo = response['check_memo']

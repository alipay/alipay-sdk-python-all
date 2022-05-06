#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerZmcardInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerZmcardInfoQueryResponse, self).__init__()
        self._credit_level = None
        self._level_code = None
        self._skip_url = None
        self._sub_code = None

    @property
    def credit_level(self):
        return self._credit_level

    @credit_level.setter
    def credit_level(self, value):
        self._credit_level = value
    @property
    def level_code(self):
        return self._level_code

    @level_code.setter
    def level_code(self, value):
        self._level_code = value
    @property
    def skip_url(self):
        return self._skip_url

    @skip_url.setter
    def skip_url(self, value):
        self._skip_url = value
    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerZmcardInfoQueryResponse, self).parse_response_content(response_content)
        if 'credit_level' in response:
            self.credit_level = response['credit_level']
        if 'level_code' in response:
            self.level_code = response['level_code']
        if 'skip_url' in response:
            self.skip_url = response['skip_url']
        if 'sub_code' in response:
            self.sub_code = response['sub_code']

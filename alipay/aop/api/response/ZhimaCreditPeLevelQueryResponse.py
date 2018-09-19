#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeLevelQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeLevelQueryResponse, self).__init__()
        self._biz_no = None
        self._level_code = None
        self._level_name = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def level_code(self):
        return self._level_code

    @level_code.setter
    def level_code(self, value):
        self._level_code = value
    @property
    def level_name(self):
        return self._level_name

    @level_name.setter
    def level_name(self, value):
        self._level_name = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeLevelQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'level_code' in response:
            self.level_code = response['level_code']
        if 'level_name' in response:
            self.level_name = response['level_name']

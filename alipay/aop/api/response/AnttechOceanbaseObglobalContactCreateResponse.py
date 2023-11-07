#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalContactCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalContactCreateResponse, self).__init__()
        self._biz_error_code = None
        self._biz_error_msg = None
        self._biz_success = None

    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def biz_error_msg(self):
        return self._biz_error_msg

    @biz_error_msg.setter
    def biz_error_msg(self, value):
        self._biz_error_msg = value
    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalContactCreateResponse, self).parse_response_content(response_content)
        if 'biz_error_code' in response:
            self.biz_error_code = response['biz_error_code']
        if 'biz_error_msg' in response:
            self.biz_error_msg = response['biz_error_msg']
        if 'biz_success' in response:
            self.biz_success = response['biz_success']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransCollectSinglemoneytokenCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransCollectSinglemoneytokenCreateResponse, self).__init__()
        self._ext_param = None
        self._qr_code = None
        self._zhi_token = None

    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def zhi_token(self):
        return self._zhi_token

    @zhi_token.setter
    def zhi_token(self, value):
        self._zhi_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransCollectSinglemoneytokenCreateResponse, self).parse_response_content(response_content)
        if 'ext_param' in response:
            self.ext_param = response['ext_param']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'zhi_token' in response:
            self.zhi_token = response['zhi_token']

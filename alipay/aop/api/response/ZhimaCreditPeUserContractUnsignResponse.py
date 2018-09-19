#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserContractUnsignResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserContractUnsignResponse, self).__init__()
        self._operate_time = None
        self._sign_id = None

    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def sign_id(self):
        return self._sign_id

    @sign_id.setter
    def sign_id(self, value):
        self._sign_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserContractUnsignResponse, self).parse_response_content(response_content)
        if 'operate_time' in response:
            self.operate_time = response['operate_time']
        if 'sign_id' in response:
            self.sign_id = response['sign_id']

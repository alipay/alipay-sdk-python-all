#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectSourceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectSourceQueryResponse, self).__init__()
        self._indirect_level = None
        self._merchant_confirm_pid = None

    @property
    def indirect_level(self):
        return self._indirect_level

    @indirect_level.setter
    def indirect_level(self, value):
        self._indirect_level = value
    @property
    def merchant_confirm_pid(self):
        return self._merchant_confirm_pid

    @merchant_confirm_pid.setter
    def merchant_confirm_pid(self, value):
        self._merchant_confirm_pid = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectSourceQueryResponse, self).parse_response_content(response_content)
        if 'indirect_level' in response:
            self.indirect_level = response['indirect_level']
        if 'merchant_confirm_pid' in response:
            self.merchant_confirm_pid = response['merchant_confirm_pid']

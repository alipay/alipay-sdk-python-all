#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandAeactivityPlatformQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandAeactivityPlatformQueryResponse, self).__init__()
        self._sign_up_status = None

    @property
    def sign_up_status(self):
        return self._sign_up_status

    @sign_up_status.setter
    def sign_up_status(self, value):
        self._sign_up_status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandAeactivityPlatformQueryResponse, self).parse_response_content(response_content)
        if 'sign_up_status' in response:
            self.sign_up_status = response['sign_up_status']

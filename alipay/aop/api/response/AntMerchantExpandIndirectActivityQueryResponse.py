#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectActivityQueryResponse, self).__init__()
        self._rate = None
        self._status = None

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectActivityQueryResponse, self).parse_response_content(response_content)
        if 'rate' in response:
            self.rate = response['rate']
        if 'status' in response:
            self.status = response['status']

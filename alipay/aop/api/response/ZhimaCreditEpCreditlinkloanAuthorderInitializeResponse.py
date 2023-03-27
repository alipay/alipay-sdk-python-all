#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpCreditlinkloanAuthorderInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpCreditlinkloanAuthorderInitializeResponse, self).__init__()
        self._merchant_biz_no = None

    @property
    def merchant_biz_no(self):
        return self._merchant_biz_no

    @merchant_biz_no.setter
    def merchant_biz_no(self, value):
        self._merchant_biz_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpCreditlinkloanAuthorderInitializeResponse, self).parse_response_content(response_content)
        if 'merchant_biz_no' in response:
            self.merchant_biz_no = response['merchant_biz_no']

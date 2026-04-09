#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantEscrowApplyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantEscrowApplyResponse, self).__init__()
        self._ant_merchant_order_no = None
        self._out_request_no = None

    @property
    def ant_merchant_order_no(self):
        return self._ant_merchant_order_no

    @ant_merchant_order_no.setter
    def ant_merchant_order_no(self, value):
        self._ant_merchant_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantEscrowApplyResponse, self).parse_response_content(response_content)
        if 'ant_merchant_order_no' in response:
            self.ant_merchant_order_no = response['ant_merchant_order_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']

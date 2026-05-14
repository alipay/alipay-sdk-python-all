#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantEscrowApplyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantEscrowApplyModifyResponse, self).__init__()
        self._ant_merchant_order_no = None
        self._ant_merchant_request_id = None
        self._out_request_no = None

    @property
    def ant_merchant_order_no(self):
        return self._ant_merchant_order_no

    @ant_merchant_order_no.setter
    def ant_merchant_order_no(self, value):
        self._ant_merchant_order_no = value
    @property
    def ant_merchant_request_id(self):
        return self._ant_merchant_request_id

    @ant_merchant_request_id.setter
    def ant_merchant_request_id(self, value):
        self._ant_merchant_request_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantEscrowApplyModifyResponse, self).parse_response_content(response_content)
        if 'ant_merchant_order_no' in response:
            self.ant_merchant_order_no = response['ant_merchant_order_no']
        if 'ant_merchant_request_id' in response:
            self.ant_merchant_request_id = response['ant_merchant_request_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditOrderRepaymentApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditOrderRepaymentApplyResponse, self).__init__()
        self._out_order_no = None
        self._success = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditOrderRepaymentApplyResponse, self).parse_response_content(response_content)
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'success' in response:
            self.success = response['success']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationBizfeeAftechCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationBizfeeAftechCreateandpayResponse, self).__init__()
        self._fee_order_no = None
        self._gmt_pay = None
        self._result_code = None
        self._result_message = None

    @property
    def fee_order_no(self):
        return self._fee_order_no

    @fee_order_no.setter
    def fee_order_no(self, value):
        self._fee_order_no = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationBizfeeAftechCreateandpayResponse, self).parse_response_content(response_content)
        if 'fee_order_no' in response:
            self.fee_order_no = response['fee_order_no']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']

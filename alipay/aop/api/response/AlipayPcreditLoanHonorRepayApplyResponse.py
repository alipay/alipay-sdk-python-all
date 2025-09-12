#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorRepayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorRepayApplyResponse, self).__init__()
        self._order_info = None
        self._out_repay_no = None
        self._refuse_code = None
        self._refuse_msg = None

    @property
    def order_info(self):
        return self._order_info

    @order_info.setter
    def order_info(self, value):
        self._order_info = value
    @property
    def out_repay_no(self):
        return self._out_repay_no

    @out_repay_no.setter
    def out_repay_no(self, value):
        self._out_repay_no = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorRepayApplyResponse, self).parse_response_content(response_content)
        if 'order_info' in response:
            self.order_info = response['order_info']
        if 'out_repay_no' in response:
            self.out_repay_no = response['out_repay_no']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorLendApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorLendApplyResponse, self).__init__()
        self._out_order_no = None
        self._refuse_code = None
        self._refuse_msg = None
        self._refuse_msg_data = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorLendApplyResponse, self).parse_response_content(response_content)
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'refuse_msg_data' in response:
            self.refuse_msg_data = response['refuse_msg_data']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUserCreditFreezeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUserCreditFreezeResponse, self).__init__()
        self._out_request_no = None
        self._success = None
        self._total_credit_amount = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def total_credit_amount(self):
        return self._total_credit_amount

    @total_credit_amount.setter
    def total_credit_amount(self, value):
        self._total_credit_amount = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUserCreditFreezeResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'success' in response:
            self.success = response['success']
        if 'total_credit_amount' in response:
            self.total_credit_amount = response['total_credit_amount']

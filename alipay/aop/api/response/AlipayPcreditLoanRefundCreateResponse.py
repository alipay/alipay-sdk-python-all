#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanRefundCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanRefundCreateResponse, self).__init__()
        self._loan_repay_no = None

    @property
    def loan_repay_no(self):
        return self._loan_repay_no

    @loan_repay_no.setter
    def loan_repay_no(self, value):
        self._loan_repay_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanRefundCreateResponse, self).parse_response_content(response_content)
        if 'loan_repay_no' in response:
            self.loan_repay_no = response['loan_repay_no']

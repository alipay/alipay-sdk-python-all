#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanRepayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanRepayApplyResponse, self).__init__()
        self._redirect_url = None
        self._repay_receipt_no = None

    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def repay_receipt_no(self):
        return self._repay_receipt_no

    @repay_receipt_no.setter
    def repay_receipt_no(self, value):
        self._repay_receipt_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanRepayApplyResponse, self).parse_response_content(response_content)
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']
        if 'repay_receipt_no' in response:
            self.repay_receipt_no = response['repay_receipt_no']

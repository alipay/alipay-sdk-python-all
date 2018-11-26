#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanCreditApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanCreditApplyResponse, self).__init__()
        self._credit_receipt_no = None
        self._redirect_url = None

    @property
    def credit_receipt_no(self):
        return self._credit_receipt_no

    @credit_receipt_no.setter
    def credit_receipt_no(self, value):
        self._credit_receipt_no = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanCreditApplyResponse, self).parse_response_content(response_content)
        if 'credit_receipt_no' in response:
            self.credit_receipt_no = response['credit_receipt_no']
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']

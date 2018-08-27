#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeLoanarCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanarCreateResponse, self).__init__()
        self._loan_ar_no = None

    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanarCreateResponse, self).parse_response_content(response_content)
        if 'loan_ar_no' in response:
            self.loan_ar_no = response['loan_ar_no']

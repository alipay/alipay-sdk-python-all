#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeNewloanarRepayApplyResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeNewloanarRepayApplyResponse, self).__init__()
        self._ev_seq_no = None
        self._loan_ar_no = None

    @property
    def ev_seq_no(self):
        return self._ev_seq_no

    @ev_seq_no.setter
    def ev_seq_no(self, value):
        self._ev_seq_no = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeNewloanarRepayApplyResponse, self).parse_response_content(response_content)
        if 'ev_seq_no' in response:
            self.ev_seq_no = response['ev_seq_no']
        if 'loan_ar_no' in response:
            self.loan_ar_no = response['loan_ar_no']

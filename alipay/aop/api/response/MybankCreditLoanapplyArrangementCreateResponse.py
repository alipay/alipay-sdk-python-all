#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyArrangementCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyArrangementCreateResponse, self).__init__()
        self._account_no = None
        self._ar_no = None
        self._ev_seq_no = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def ev_seq_no(self):
        return self._ev_seq_no

    @ev_seq_no.setter
    def ev_seq_no(self, value):
        self._ev_seq_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyArrangementCreateResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
        if 'ev_seq_no' in response:
            self.ev_seq_no = response['ev_seq_no']

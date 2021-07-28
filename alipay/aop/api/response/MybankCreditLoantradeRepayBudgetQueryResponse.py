#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeRepayBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeRepayBudgetQueryResponse, self).__init__()
        self._apply_repay_prin = None
        self._loan_ar_no = None
        self._should_repay_fee = None
        self._should_repay_int = None
        self._should_repay_penalty = None
        self._should_repay_pre_fee = None
        self._should_repay_prin = None

    @property
    def apply_repay_prin(self):
        return self._apply_repay_prin

    @apply_repay_prin.setter
    def apply_repay_prin(self, value):
        self._apply_repay_prin = value
    @property
    def loan_ar_no(self):
        return self._loan_ar_no

    @loan_ar_no.setter
    def loan_ar_no(self, value):
        self._loan_ar_no = value
    @property
    def should_repay_fee(self):
        return self._should_repay_fee

    @should_repay_fee.setter
    def should_repay_fee(self, value):
        self._should_repay_fee = value
    @property
    def should_repay_int(self):
        return self._should_repay_int

    @should_repay_int.setter
    def should_repay_int(self, value):
        self._should_repay_int = value
    @property
    def should_repay_penalty(self):
        return self._should_repay_penalty

    @should_repay_penalty.setter
    def should_repay_penalty(self, value):
        self._should_repay_penalty = value
    @property
    def should_repay_pre_fee(self):
        return self._should_repay_pre_fee

    @should_repay_pre_fee.setter
    def should_repay_pre_fee(self, value):
        self._should_repay_pre_fee = value
    @property
    def should_repay_prin(self):
        return self._should_repay_prin

    @should_repay_prin.setter
    def should_repay_prin(self, value):
        self._should_repay_prin = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeRepayBudgetQueryResponse, self).parse_response_content(response_content)
        if 'apply_repay_prin' in response:
            self.apply_repay_prin = response['apply_repay_prin']
        if 'loan_ar_no' in response:
            self.loan_ar_no = response['loan_ar_no']
        if 'should_repay_fee' in response:
            self.should_repay_fee = response['should_repay_fee']
        if 'should_repay_int' in response:
            self.should_repay_int = response['should_repay_int']
        if 'should_repay_penalty' in response:
            self.should_repay_penalty = response['should_repay_penalty']
        if 'should_repay_pre_fee' in response:
            self.should_repay_pre_fee = response['should_repay_pre_fee']
        if 'should_repay_prin' in response:
            self.should_repay_prin = response['should_repay_prin']

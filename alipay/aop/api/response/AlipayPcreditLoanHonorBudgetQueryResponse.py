#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorBudgetQueryResponse, self).__init__()
        self._fee_rate = None
        self._total_amount = None
        self._total_interest = None
        self._total_penalty = None
        self._total_principal = None
        self._total_violate_fee = None

    @property
    def fee_rate(self):
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, value):
        self._fee_rate = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_interest(self):
        return self._total_interest

    @total_interest.setter
    def total_interest(self, value):
        self._total_interest = value
    @property
    def total_penalty(self):
        return self._total_penalty

    @total_penalty.setter
    def total_penalty(self, value):
        self._total_penalty = value
    @property
    def total_principal(self):
        return self._total_principal

    @total_principal.setter
    def total_principal(self, value):
        self._total_principal = value
    @property
    def total_violate_fee(self):
        return self._total_violate_fee

    @total_violate_fee.setter
    def total_violate_fee(self, value):
        self._total_violate_fee = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorBudgetQueryResponse, self).parse_response_content(response_content)
        if 'fee_rate' in response:
            self.fee_rate = response['fee_rate']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_interest' in response:
            self.total_interest = response['total_interest']
        if 'total_penalty' in response:
            self.total_penalty = response['total_penalty']
        if 'total_principal' in response:
            self.total_principal = response['total_principal']
        if 'total_violate_fee' in response:
            self.total_violate_fee = response['total_violate_fee']

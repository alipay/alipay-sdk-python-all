#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanHonorBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorBudgetQueryResponse, self).__init__()
        self._total_amount = None
        self._total_interest = None
        self._total_penalty = None
        self._total_principal = None

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

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorBudgetQueryResponse, self).parse_response_content(response_content)
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_interest' in response:
            self.total_interest = response['total_interest']
        if 'total_penalty' in response:
            self.total_penalty = response['total_penalty']
        if 'total_principal' in response:
            self.total_principal = response['total_principal']

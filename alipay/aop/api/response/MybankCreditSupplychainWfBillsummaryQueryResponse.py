#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf


class MybankCreditSupplychainWfBillsummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfBillsummaryQueryResponse, self).__init__()
        self._balanceamt = None
        self._ovdamt = None
        self._status = None

    @property
    def balanceamt(self):
        return self._balanceamt

    @balanceamt.setter
    def balanceamt(self, value):
        if isinstance(value, AmountWf):
            self._balanceamt = value
        else:
            self._balanceamt = AmountWf.from_alipay_dict(value)
    @property
    def ovdamt(self):
        return self._ovdamt

    @ovdamt.setter
    def ovdamt(self, value):
        if isinstance(value, AmountWf):
            self._ovdamt = value
        else:
            self._ovdamt = AmountWf.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfBillsummaryQueryResponse, self).parse_response_content(response_content)
        if 'balanceamt' in response:
            self.balanceamt = response['balanceamt']
        if 'ovdamt' in response:
            self.ovdamt = response['ovdamt']
        if 'status' in response:
            self.status = response['status']

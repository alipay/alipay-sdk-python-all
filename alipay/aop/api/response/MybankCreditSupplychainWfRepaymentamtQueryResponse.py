#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmountWf import AmountWf


class MybankCreditSupplychainWfRepaymentamtQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfRepaymentamtQueryResponse, self).__init__()
        self._totalbalance = None

    @property
    def totalbalance(self):
        return self._totalbalance

    @totalbalance.setter
    def totalbalance(self, value):
        if isinstance(value, AmountWf):
            self._totalbalance = value
        else:
            self._totalbalance = AmountWf.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfRepaymentamtQueryResponse, self).parse_response_content(response_content)
        if 'totalbalance' in response:
            self.totalbalance = response['totalbalance']

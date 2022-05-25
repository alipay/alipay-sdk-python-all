#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmountWf import AmountWf


class MybankCreditSupplychainWfLimitamountQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfLimitamountQueryResponse, self).__init__()
        self._admit = None
        self._limitamt = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def limitamt(self):
        return self._limitamt

    @limitamt.setter
    def limitamt(self, value):
        if isinstance(value, AmountWf):
            self._limitamt = value
        else:
            self._limitamt = AmountWf.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfLimitamountQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'limitamt' in response:
            self.limitamt = response['limitamt']

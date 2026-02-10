#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeLoanstatusAdmitQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanstatusAdmitQueryResponse, self).__init__()
        self._authority = None
        self._credit_admit = None
        self._has_balance = None

    @property
    def authority(self):
        return self._authority

    @authority.setter
    def authority(self, value):
        self._authority = value
    @property
    def credit_admit(self):
        return self._credit_admit

    @credit_admit.setter
    def credit_admit(self, value):
        self._credit_admit = value
    @property
    def has_balance(self):
        return self._has_balance

    @has_balance.setter
    def has_balance(self, value):
        self._has_balance = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanstatusAdmitQueryResponse, self).parse_response_content(response_content)
        if 'authority' in response:
            self.authority = response['authority']
        if 'credit_admit' in response:
            self.credit_admit = response['credit_admit']
        if 'has_balance' in response:
            self.has_balance = response['has_balance']

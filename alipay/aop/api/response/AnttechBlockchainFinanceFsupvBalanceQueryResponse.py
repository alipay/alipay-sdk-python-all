#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceFsupvBalanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFsupvBalanceQueryResponse, self).__init__()
        self._balance = None
        self._mark = None
        self._status = None

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFsupvBalanceQueryResponse, self).parse_response_content(response_content)
        if 'balance' in response:
            self.balance = response['balance']
        if 'mark' in response:
            self.mark = response['mark']
        if 'status' in response:
            self.status = response['status']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataBillAccountdailyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataBillAccountdailyQueryResponse, self).__init__()
        self._deposit_amount = None
        self._trans_in_amount = None
        self._trans_out_amount = None
        self._withdraw_amount = None

    @property
    def deposit_amount(self):
        return self._deposit_amount

    @deposit_amount.setter
    def deposit_amount(self, value):
        self._deposit_amount = value
    @property
    def trans_in_amount(self):
        return self._trans_in_amount

    @trans_in_amount.setter
    def trans_in_amount(self, value):
        self._trans_in_amount = value
    @property
    def trans_out_amount(self):
        return self._trans_out_amount

    @trans_out_amount.setter
    def trans_out_amount(self, value):
        self._trans_out_amount = value
    @property
    def withdraw_amount(self):
        return self._withdraw_amount

    @withdraw_amount.setter
    def withdraw_amount(self, value):
        self._withdraw_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataBillAccountdailyQueryResponse, self).parse_response_content(response_content)
        if 'deposit_amount' in response:
            self.deposit_amount = response['deposit_amount']
        if 'trans_in_amount' in response:
            self.trans_in_amount = response['trans_in_amount']
        if 'trans_out_amount' in response:
            self.trans_out_amount = response['trans_out_amount']
        if 'withdraw_amount' in response:
            self.withdraw_amount = response['withdraw_amount']

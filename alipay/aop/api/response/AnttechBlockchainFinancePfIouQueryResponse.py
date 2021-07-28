#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinancePfIouQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinancePfIouQueryResponse, self).__init__()
        self._credit_id = None
        self._issued_amount = None
        self._pay_in_account = None
        self._remark = None
        self._repay_account = None

    @property
    def credit_id(self):
        return self._credit_id

    @credit_id.setter
    def credit_id(self, value):
        self._credit_id = value
    @property
    def issued_amount(self):
        return self._issued_amount

    @issued_amount.setter
    def issued_amount(self, value):
        self._issued_amount = value
    @property
    def pay_in_account(self):
        return self._pay_in_account

    @pay_in_account.setter
    def pay_in_account(self, value):
        self._pay_in_account = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def repay_account(self):
        return self._repay_account

    @repay_account.setter
    def repay_account(self, value):
        self._repay_account = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinancePfIouQueryResponse, self).parse_response_content(response_content)
        if 'credit_id' in response:
            self.credit_id = response['credit_id']
        if 'issued_amount' in response:
            self.issued_amount = response['issued_amount']
        if 'pay_in_account' in response:
            self.pay_in_account = response['pay_in_account']
        if 'remark' in response:
            self.remark = response['remark']
        if 'repay_account' in response:
            self.repay_account = response['repay_account']

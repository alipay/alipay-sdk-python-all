#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementTransferResponse, self).__init__()
        self._amount = None
        self._execute_time = None
        self._period = None
        self._period_type = None
        self._total_amount = None
        self._total_payments = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_payments(self):
        return self._total_payments

    @total_payments.setter
    def total_payments(self, value):
        self._total_payments = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementTransferResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'execute_time' in response:
            self.execute_time = response['execute_time']
        if 'period' in response:
            self.period = response['period']
        if 'period_type' in response:
            self.period_type = response['period_type']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'total_payments' in response:
            self.total_payments = response['total_payments']

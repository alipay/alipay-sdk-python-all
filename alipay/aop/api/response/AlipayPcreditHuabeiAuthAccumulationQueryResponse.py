#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiAuthAccumulationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiAuthAccumulationQueryResponse, self).__init__()
        self._pay_amount = None
        self._total_discount_amount = None
        self._total_pay_count = None
        self._total_real_pay_amount = None

    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def total_discount_amount(self):
        return self._total_discount_amount

    @total_discount_amount.setter
    def total_discount_amount(self, value):
        self._total_discount_amount = value
    @property
    def total_pay_count(self):
        return self._total_pay_count

    @total_pay_count.setter
    def total_pay_count(self, value):
        self._total_pay_count = value
    @property
    def total_real_pay_amount(self):
        return self._total_real_pay_amount

    @total_real_pay_amount.setter
    def total_real_pay_amount(self, value):
        self._total_real_pay_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiAuthAccumulationQueryResponse, self).parse_response_content(response_content)
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'total_discount_amount' in response:
            self.total_discount_amount = response['total_discount_amount']
        if 'total_pay_count' in response:
            self.total_pay_count = response['total_pay_count']
        if 'total_real_pay_amount' in response:
            self.total_real_pay_amount = response['total_real_pay_amount']

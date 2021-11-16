#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserBillStatQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserBillStatQueryResponse, self).__init__()
        self._expenditure_amount = None
        self._income_amount = None

    @property
    def expenditure_amount(self):
        return self._expenditure_amount

    @expenditure_amount.setter
    def expenditure_amount(self, value):
        self._expenditure_amount = value
    @property
    def income_amount(self):
        return self._income_amount

    @income_amount.setter
    def income_amount(self, value):
        self._income_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserBillStatQueryResponse, self).parse_response_content(response_content)
        if 'expenditure_amount' in response:
            self.expenditure_amount = response['expenditure_amount']
        if 'income_amount' in response:
            self.income_amount = response['income_amount']

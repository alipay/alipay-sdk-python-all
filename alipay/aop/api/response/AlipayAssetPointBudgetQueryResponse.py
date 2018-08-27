#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointBudgetQueryResponse, self).__init__()
        self._budget_amount = None

    @property
    def budget_amount(self):
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, value):
        self._budget_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointBudgetQueryResponse, self).parse_response_content(response_content)
        if 'budget_amount' in response:
            self.budget_amount = response['budget_amount']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingEquityBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingEquityBudgetQueryResponse, self).__init__()
        self._remaining_budget = None
        self._total_budget = None

    @property
    def remaining_budget(self):
        return self._remaining_budget

    @remaining_budget.setter
    def remaining_budget(self, value):
        self._remaining_budget = value
    @property
    def total_budget(self):
        return self._total_budget

    @total_budget.setter
    def total_budget(self, value):
        self._total_budget = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingEquityBudgetQueryResponse, self).parse_response_content(response_content)
        if 'remaining_budget' in response:
            self.remaining_budget = response['remaining_budget']
        if 'total_budget' in response:
            self.total_budget = response['total_budget']

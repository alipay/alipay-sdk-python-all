#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsMarketingExperienceAccountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingExperienceAccountQueryResponse, self).__init__()
        self._remaining_profit = None
        self._total_experience_amount = None

    @property
    def remaining_profit(self):
        return self._remaining_profit

    @remaining_profit.setter
    def remaining_profit(self, value):
        self._remaining_profit = value
    @property
    def total_experience_amount(self):
        return self._total_experience_amount

    @total_experience_amount.setter
    def total_experience_amount(self, value):
        self._total_experience_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingExperienceAccountQueryResponse, self).parse_response_content(response_content)
        if 'remaining_profit' in response:
            self.remaining_profit = response['remaining_profit']
        if 'total_experience_amount' in response:
            self.total_experience_amount = response['total_experience_amount']

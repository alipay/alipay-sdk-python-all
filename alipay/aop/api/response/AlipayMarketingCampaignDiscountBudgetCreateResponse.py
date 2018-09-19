#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDiscountBudgetCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDiscountBudgetCreateResponse, self).__init__()
        self._budget_id = None

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDiscountBudgetCreateResponse, self).parse_response_content(response_content)
        if 'budget_id' in response:
            self.budget_id = response['budget_id']

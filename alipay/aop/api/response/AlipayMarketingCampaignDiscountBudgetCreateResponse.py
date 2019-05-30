#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDiscountBudgetCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDiscountBudgetCreateResponse, self).__init__()
        self._budget_id = None
        self._confirm_uri = None
        self._fund_order_no = None

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value
    @property
    def confirm_uri(self):
        return self._confirm_uri

    @confirm_uri.setter
    def confirm_uri(self, value):
        self._confirm_uri = value
    @property
    def fund_order_no(self):
        return self._fund_order_no

    @fund_order_no.setter
    def fund_order_no(self, value):
        self._fund_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDiscountBudgetCreateResponse, self).parse_response_content(response_content)
        if 'budget_id' in response:
            self.budget_id = response['budget_id']
        if 'confirm_uri' in response:
            self.confirm_uri = response['confirm_uri']
        if 'fund_order_no' in response:
            self.fund_order_no = response['fund_order_no']

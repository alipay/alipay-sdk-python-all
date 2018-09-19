#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignDiscountBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignDiscountBudgetQueryResponse, self).__init__()
        self._budget_id = None
        self._freeze_amount = None
        self._recycle_amount = None
        self._refund_amount = None
        self._total_amount = None
        self._used_amount = None

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def recycle_amount(self):
        return self._recycle_amount

    @recycle_amount.setter
    def recycle_amount(self, value):
        self._recycle_amount = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def used_amount(self):
        return self._used_amount

    @used_amount.setter
    def used_amount(self, value):
        self._used_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignDiscountBudgetQueryResponse, self).parse_response_content(response_content)
        if 'budget_id' in response:
            self.budget_id = response['budget_id']
        if 'freeze_amount' in response:
            self.freeze_amount = response['freeze_amount']
        if 'recycle_amount' in response:
            self.recycle_amount = response['recycle_amount']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'used_amount' in response:
            self.used_amount = response['used_amount']

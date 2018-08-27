#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignDiscountBudgetAppendModel(object):

    def __init__(self):
        self._budget_id = None
        self._total_amount = None

    @property
    def budget_id(self):
        return self._budget_id

    @budget_id.setter
    def budget_id(self, value):
        self._budget_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_id:
            if hasattr(self.budget_id, 'to_alipay_dict'):
                params['budget_id'] = self.budget_id.to_alipay_dict()
            else:
                params['budget_id'] = self.budget_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDiscountBudgetAppendModel()
        if 'budget_id' in d:
            o.budget_id = d['budget_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



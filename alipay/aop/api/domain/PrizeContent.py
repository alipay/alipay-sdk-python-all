#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeContent(object):

    def __init__(self):
        self._prize_budget = None
        self._prize_id = None
        self._prize_name = None
        self._prize_price = None

    @property
    def prize_budget(self):
        return self._prize_budget

    @prize_budget.setter
    def prize_budget(self, value):
        self._prize_budget = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_price(self):
        return self._prize_price

    @prize_price.setter
    def prize_price(self, value):
        self._prize_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.prize_budget:
            if hasattr(self.prize_budget, 'to_alipay_dict'):
                params['prize_budget'] = self.prize_budget.to_alipay_dict()
            else:
                params['prize_budget'] = self.prize_budget
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_price:
            if hasattr(self.prize_price, 'to_alipay_dict'):
                params['prize_price'] = self.prize_price.to_alipay_dict()
            else:
                params['prize_price'] = self.prize_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeContent()
        if 'prize_budget' in d:
            o.prize_budget = d['prize_budget']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_price' in d:
            o.prize_price = d['prize_price']
        return o



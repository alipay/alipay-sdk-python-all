#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherPackageSalesInfo(object):

    def __init__(self):
        self._budget = None
        self._pay_channel = None
        self._purchase_url = None
        self._sale_count_limit_in_period = None
        self._sale_period_limit = None
        self._sale_price = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def purchase_url(self):
        return self._purchase_url

    @purchase_url.setter
    def purchase_url(self, value):
        self._purchase_url = value
    @property
    def sale_count_limit_in_period(self):
        return self._sale_count_limit_in_period

    @sale_count_limit_in_period.setter
    def sale_count_limit_in_period(self, value):
        self._sale_count_limit_in_period = value
    @property
    def sale_period_limit(self):
        return self._sale_period_limit

    @sale_period_limit.setter
    def sale_period_limit(self, value):
        self._sale_period_limit = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.purchase_url:
            if hasattr(self.purchase_url, 'to_alipay_dict'):
                params['purchase_url'] = self.purchase_url.to_alipay_dict()
            else:
                params['purchase_url'] = self.purchase_url
        if self.sale_count_limit_in_period:
            if hasattr(self.sale_count_limit_in_period, 'to_alipay_dict'):
                params['sale_count_limit_in_period'] = self.sale_count_limit_in_period.to_alipay_dict()
            else:
                params['sale_count_limit_in_period'] = self.sale_count_limit_in_period
        if self.sale_period_limit:
            if hasattr(self.sale_period_limit, 'to_alipay_dict'):
                params['sale_period_limit'] = self.sale_period_limit.to_alipay_dict()
            else:
                params['sale_period_limit'] = self.sale_period_limit
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageSalesInfo()
        if 'budget' in d:
            o.budget = d['budget']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'purchase_url' in d:
            o.purchase_url = d['purchase_url']
        if 'sale_count_limit_in_period' in d:
            o.sale_count_limit_in_period = d['sale_count_limit_in_period']
        if 'sale_period_limit' in d:
            o.sale_period_limit = d['sale_period_limit']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        return o



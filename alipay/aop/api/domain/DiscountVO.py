#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountVO(object):

    def __init__(self):
        self._activity_code = None
        self._activity_id = None
        self._amount_discount = None
        self._platform_cost = None
        self._seller_cost = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def amount_discount(self):
        return self._amount_discount

    @amount_discount.setter
    def amount_discount(self, value):
        self._amount_discount = value
    @property
    def platform_cost(self):
        return self._platform_cost

    @platform_cost.setter
    def platform_cost(self, value):
        self._platform_cost = value
    @property
    def seller_cost(self):
        return self._seller_cost

    @seller_cost.setter
    def seller_cost(self, value):
        self._seller_cost = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.amount_discount:
            if hasattr(self.amount_discount, 'to_alipay_dict'):
                params['amount_discount'] = self.amount_discount.to_alipay_dict()
            else:
                params['amount_discount'] = self.amount_discount
        if self.platform_cost:
            if hasattr(self.platform_cost, 'to_alipay_dict'):
                params['platform_cost'] = self.platform_cost.to_alipay_dict()
            else:
                params['platform_cost'] = self.platform_cost
        if self.seller_cost:
            if hasattr(self.seller_cost, 'to_alipay_dict'):
                params['seller_cost'] = self.seller_cost.to_alipay_dict()
            else:
                params['seller_cost'] = self.seller_cost
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountVO()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'amount_discount' in d:
            o.amount_discount = d['amount_discount']
        if 'platform_cost' in d:
            o.platform_cost = d['platform_cost']
        if 'seller_cost' in d:
            o.seller_cost = d['seller_cost']
        return o



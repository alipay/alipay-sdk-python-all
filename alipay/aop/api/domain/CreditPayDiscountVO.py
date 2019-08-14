#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayDiscountVO(object):

    def __init__(self):
        self._discount_desc = None
        self._discount_name = None
        self._full_discount_rate = None
        self._has_discount = None
        self._is_uneven_discount = None

    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def full_discount_rate(self):
        return self._full_discount_rate

    @full_discount_rate.setter
    def full_discount_rate(self, value):
        self._full_discount_rate = value
    @property
    def has_discount(self):
        return self._has_discount

    @has_discount.setter
    def has_discount(self, value):
        self._has_discount = value
    @property
    def is_uneven_discount(self):
        return self._is_uneven_discount

    @is_uneven_discount.setter
    def is_uneven_discount(self, value):
        self._is_uneven_discount = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.discount_name:
            if hasattr(self.discount_name, 'to_alipay_dict'):
                params['discount_name'] = self.discount_name.to_alipay_dict()
            else:
                params['discount_name'] = self.discount_name
        if self.full_discount_rate:
            if hasattr(self.full_discount_rate, 'to_alipay_dict'):
                params['full_discount_rate'] = self.full_discount_rate.to_alipay_dict()
            else:
                params['full_discount_rate'] = self.full_discount_rate
        if self.has_discount:
            if hasattr(self.has_discount, 'to_alipay_dict'):
                params['has_discount'] = self.has_discount.to_alipay_dict()
            else:
                params['has_discount'] = self.has_discount
        if self.is_uneven_discount:
            if hasattr(self.is_uneven_discount, 'to_alipay_dict'):
                params['is_uneven_discount'] = self.is_uneven_discount.to_alipay_dict()
            else:
                params['is_uneven_discount'] = self.is_uneven_discount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayDiscountVO()
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'discount_name' in d:
            o.discount_name = d['discount_name']
        if 'full_discount_rate' in d:
            o.full_discount_rate = d['full_discount_rate']
        if 'has_discount' in d:
            o.has_discount = d['has_discount']
        if 'is_uneven_discount' in d:
            o.is_uneven_discount = d['is_uneven_discount']
        return o



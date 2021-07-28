#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiscountTypeSyncData(object):

    def __init__(self):
        self._discount_amount = None
        self._discount_desc = None

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiscountTypeSyncData()
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        return o



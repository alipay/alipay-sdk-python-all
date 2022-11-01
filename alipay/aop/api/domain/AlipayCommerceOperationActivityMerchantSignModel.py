#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationActivityMerchantSignModel(object):

    def __init__(self):
        self._consumption_threshold = None
        self._discount_amount = None
        self._type = None

    @property
    def consumption_threshold(self):
        return self._consumption_threshold

    @consumption_threshold.setter
    def consumption_threshold(self, value):
        self._consumption_threshold = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.consumption_threshold:
            if hasattr(self.consumption_threshold, 'to_alipay_dict'):
                params['consumption_threshold'] = self.consumption_threshold.to_alipay_dict()
            else:
                params['consumption_threshold'] = self.consumption_threshold
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationActivityMerchantSignModel()
        if 'consumption_threshold' in d:
            o.consumption_threshold = d['consumption_threshold']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'type' in d:
            o.type = d['type']
        return o



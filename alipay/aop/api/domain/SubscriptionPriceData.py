#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionProductData import SubscriptionProductData
from alipay.aop.api.domain.SubscriptionRecurring import SubscriptionRecurring


class SubscriptionPriceData(object):

    def __init__(self):
        self._metadata = None
        self._product_data = None
        self._recurring = None
        self._unit_amount = None

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def product_data(self):
        return self._product_data

    @product_data.setter
    def product_data(self, value):
        if isinstance(value, SubscriptionProductData):
            self._product_data = value
        else:
            self._product_data = SubscriptionProductData.from_alipay_dict(value)
    @property
    def recurring(self):
        return self._recurring

    @recurring.setter
    def recurring(self, value):
        if isinstance(value, SubscriptionRecurring):
            self._recurring = value
        else:
            self._recurring = SubscriptionRecurring.from_alipay_dict(value)
    @property
    def unit_amount(self):
        return self._unit_amount

    @unit_amount.setter
    def unit_amount(self, value):
        self._unit_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.product_data:
            if hasattr(self.product_data, 'to_alipay_dict'):
                params['product_data'] = self.product_data.to_alipay_dict()
            else:
                params['product_data'] = self.product_data
        if self.recurring:
            if hasattr(self.recurring, 'to_alipay_dict'):
                params['recurring'] = self.recurring.to_alipay_dict()
            else:
                params['recurring'] = self.recurring
        if self.unit_amount:
            if hasattr(self.unit_amount, 'to_alipay_dict'):
                params['unit_amount'] = self.unit_amount.to_alipay_dict()
            else:
                params['unit_amount'] = self.unit_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscriptionPriceData()
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'product_data' in d:
            o.product_data = d['product_data']
        if 'recurring' in d:
            o.recurring = d['recurring']
        if 'unit_amount' in d:
            o.unit_amount = d['unit_amount']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalShopMarketingActivityRule(object):

    def __init__(self):
        self._reduce_price = None
        self._reduce_price_threshold = None

    @property
    def reduce_price(self):
        return self._reduce_price

    @reduce_price.setter
    def reduce_price(self, value):
        self._reduce_price = value
    @property
    def reduce_price_threshold(self):
        return self._reduce_price_threshold

    @reduce_price_threshold.setter
    def reduce_price_threshold(self, value):
        self._reduce_price_threshold = value


    def to_alipay_dict(self):
        params = dict()
        if self.reduce_price:
            if hasattr(self.reduce_price, 'to_alipay_dict'):
                params['reduce_price'] = self.reduce_price.to_alipay_dict()
            else:
                params['reduce_price'] = self.reduce_price
        if self.reduce_price_threshold:
            if hasattr(self.reduce_price_threshold, 'to_alipay_dict'):
                params['reduce_price_threshold'] = self.reduce_price_threshold.to_alipay_dict()
            else:
                params['reduce_price_threshold'] = self.reduce_price_threshold
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalShopMarketingActivityRule()
        if 'reduce_price' in d:
            o.reduce_price = d['reduce_price']
        if 'reduce_price_threshold' in d:
            o.reduce_price_threshold = d['reduce_price_threshold']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardEachPromoInfo(object):

    def __init__(self):
        self._each_promo_price = None
        self._period = None

    @property
    def each_promo_price(self):
        return self._each_promo_price

    @each_promo_price.setter
    def each_promo_price(self, value):
        self._each_promo_price = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value


    def to_alipay_dict(self):
        params = dict()
        if self.each_promo_price:
            if hasattr(self.each_promo_price, 'to_alipay_dict'):
                params['each_promo_price'] = self.each_promo_price.to_alipay_dict()
            else:
                params['each_promo_price'] = self.each_promo_price
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardEachPromoInfo()
        if 'each_promo_price' in d:
            o.each_promo_price = d['each_promo_price']
        if 'period' in d:
            o.period = d['period']
        return o



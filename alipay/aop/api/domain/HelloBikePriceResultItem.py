#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HelloBikePriceResultItem(object):

    def __init__(self):
        self._card_type = None
        self._promo_price_cent = None

    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def promo_price_cent(self):
        return self._promo_price_cent

    @promo_price_cent.setter
    def promo_price_cent(self, value):
        self._promo_price_cent = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.promo_price_cent:
            if hasattr(self.promo_price_cent, 'to_alipay_dict'):
                params['promo_price_cent'] = self.promo_price_cent.to_alipay_dict()
            else:
                params['promo_price_cent'] = self.promo_price_cent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HelloBikePriceResultItem()
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'promo_price_cent' in d:
            o.promo_price_cent = d['promo_price_cent']
        return o



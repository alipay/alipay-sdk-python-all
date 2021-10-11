#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaidOuterCardPriceDetailDTO(object):

    def __init__(self):
        self._desc = None
        self._price = None
        self._price_type = None
        self._worth = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def price_type(self):
        return self._price_type

    @price_type.setter
    def price_type(self, value):
        self._price_type = value
    @property
    def worth(self):
        return self._worth

    @worth.setter
    def worth(self, value):
        self._worth = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.price_type:
            if hasattr(self.price_type, 'to_alipay_dict'):
                params['price_type'] = self.price_type.to_alipay_dict()
            else:
                params['price_type'] = self.price_type
        if self.worth:
            if hasattr(self.worth, 'to_alipay_dict'):
                params['worth'] = self.worth.to_alipay_dict()
            else:
                params['worth'] = self.worth
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaidOuterCardPriceDetailDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'price' in d:
            o.price = d['price']
        if 'price_type' in d:
            o.price_type = d['price_type']
        if 'worth' in d:
            o.worth = d['worth']
        return o



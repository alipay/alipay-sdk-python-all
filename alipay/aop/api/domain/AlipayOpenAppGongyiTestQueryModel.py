#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdvertItem import AdvertItem


class AlipayOpenAppGongyiTestQueryModel(object):

    def __init__(self):
        self._asdf = None
        self._count = None
        self._price = None

    @property
    def asdf(self):
        return self._asdf

    @asdf.setter
    def asdf(self, value):
        if isinstance(value, AdvertItem):
            self._asdf = value
        else:
            self._asdf = AdvertItem.from_alipay_dict(value)
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.asdf:
            if hasattr(self.asdf, 'to_alipay_dict'):
                params['asdf'] = self.asdf.to_alipay_dict()
            else:
                params['asdf'] = self.asdf
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppGongyiTestQueryModel()
        if 'asdf' in d:
            o.asdf = d['asdf']
        if 'count' in d:
            o.count = d['count']
        if 'price' in d:
            o.price = d['price']
        return o



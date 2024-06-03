#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HotelPromotionDetail(object):

    def __init__(self):
        self._discount = None
        self._type = None

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
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
        o = HotelPromotionDetail()
        if 'discount' in d:
            o.discount = d['discount']
        if 'type' in d:
            o.type = d['type']
        return o



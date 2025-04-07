#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyclePriceDTO import RecyclePriceDTO


class RecycleSkuCustomPriceDTO(object):

    def __init__(self):
        self._price_code = None
        self._price_value = None

    @property
    def price_code(self):
        return self._price_code

    @price_code.setter
    def price_code(self, value):
        self._price_code = value
    @property
    def price_value(self):
        return self._price_value

    @price_value.setter
    def price_value(self, value):
        if isinstance(value, RecyclePriceDTO):
            self._price_value = value
        else:
            self._price_value = RecyclePriceDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.price_code:
            if hasattr(self.price_code, 'to_alipay_dict'):
                params['price_code'] = self.price_code.to_alipay_dict()
            else:
                params['price_code'] = self.price_code
        if self.price_value:
            if hasattr(self.price_value, 'to_alipay_dict'):
                params['price_value'] = self.price_value.to_alipay_dict()
            else:
                params['price_value'] = self.price_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleSkuCustomPriceDTO()
        if 'price_code' in d:
            o.price_code = d['price_code']
        if 'price_value' in d:
            o.price_value = d['price_value']
        return o



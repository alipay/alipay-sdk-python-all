#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleDeliveryPriceDTO import RecycleDeliveryPriceDTO


class RecycleDeliveryConfigDTO(object):

    def __init__(self):
        self._delivery_price = None
        self._province_code = None

    @property
    def delivery_price(self):
        return self._delivery_price

    @delivery_price.setter
    def delivery_price(self, value):
        if isinstance(value, RecycleDeliveryPriceDTO):
            self._delivery_price = value
        else:
            self._delivery_price = RecycleDeliveryPriceDTO.from_alipay_dict(value)
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_price:
            if hasattr(self.delivery_price, 'to_alipay_dict'):
                params['delivery_price'] = self.delivery_price.to_alipay_dict()
            else:
                params['delivery_price'] = self.delivery_price
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleDeliveryConfigDTO()
        if 'delivery_price' in d:
            o.delivery_price = d['delivery_price']
        if 'province_code' in d:
            o.province_code = d['province_code']
        return o



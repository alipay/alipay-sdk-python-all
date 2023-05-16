#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AccessLadderPriceDto(object):

    def __init__(self):
        self._minimum_purchase_quantity = None
        self._origin_unit_price = None
        self._unit_price = None

    @property
    def minimum_purchase_quantity(self):
        return self._minimum_purchase_quantity

    @minimum_purchase_quantity.setter
    def minimum_purchase_quantity(self, value):
        self._minimum_purchase_quantity = value
    @property
    def origin_unit_price(self):
        return self._origin_unit_price

    @origin_unit_price.setter
    def origin_unit_price(self, value):
        self._origin_unit_price = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.minimum_purchase_quantity:
            if hasattr(self.minimum_purchase_quantity, 'to_alipay_dict'):
                params['minimum_purchase_quantity'] = self.minimum_purchase_quantity.to_alipay_dict()
            else:
                params['minimum_purchase_quantity'] = self.minimum_purchase_quantity
        if self.origin_unit_price:
            if hasattr(self.origin_unit_price, 'to_alipay_dict'):
                params['origin_unit_price'] = self.origin_unit_price.to_alipay_dict()
            else:
                params['origin_unit_price'] = self.origin_unit_price
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessLadderPriceDto()
        if 'minimum_purchase_quantity' in d:
            o.minimum_purchase_quantity = d['minimum_purchase_quantity']
        if 'origin_unit_price' in d:
            o.origin_unit_price = d['origin_unit_price']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        return o



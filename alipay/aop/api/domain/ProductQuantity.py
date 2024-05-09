#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductQuantity(object):

    def __init__(self):
        self._quantity = None
        self._unit_type = None

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def unit_type(self):
        return self._unit_type

    @unit_type.setter
    def unit_type(self, value):
        self._unit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.unit_type:
            if hasattr(self.unit_type, 'to_alipay_dict'):
                params['unit_type'] = self.unit_type.to_alipay_dict()
            else:
                params['unit_type'] = self.unit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductQuantity()
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'unit_type' in d:
            o.unit_type = d['unit_type']
        return o



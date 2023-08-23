#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeeItem(object):

    def __init__(self):
        self._fee_item_code = None
        self._fee_item_name = None
        self._quantity = None
        self._quantity_unit = None

    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def quantity_unit(self):
        return self._quantity_unit

    @quantity_unit.setter
    def quantity_unit(self, value):
        self._quantity_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.quantity_unit:
            if hasattr(self.quantity_unit, 'to_alipay_dict'):
                params['quantity_unit'] = self.quantity_unit.to_alipay_dict()
            else:
                params['quantity_unit'] = self.quantity_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeeItem()
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'quantity_unit' in d:
            o.quantity_unit = d['quantity_unit']
        return o



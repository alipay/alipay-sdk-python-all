#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MarketingProductInfo(object):

    def __init__(self):
        self._assess_amount = None
        self._assess_max_amount = None
        self._assess_max_quantity = None
        self._assess_min_amount = None
        self._assess_min_quantity = None
        self._assess_quantity = None
        self._assess_type = None
        self._inspect_amount = None
        self._inspect_quantity = None
        self._unit_type = None

    @property
    def assess_amount(self):
        return self._assess_amount

    @assess_amount.setter
    def assess_amount(self, value):
        self._assess_amount = value
    @property
    def assess_max_amount(self):
        return self._assess_max_amount

    @assess_max_amount.setter
    def assess_max_amount(self, value):
        self._assess_max_amount = value
    @property
    def assess_max_quantity(self):
        return self._assess_max_quantity

    @assess_max_quantity.setter
    def assess_max_quantity(self, value):
        self._assess_max_quantity = value
    @property
    def assess_min_amount(self):
        return self._assess_min_amount

    @assess_min_amount.setter
    def assess_min_amount(self, value):
        self._assess_min_amount = value
    @property
    def assess_min_quantity(self):
        return self._assess_min_quantity

    @assess_min_quantity.setter
    def assess_min_quantity(self, value):
        self._assess_min_quantity = value
    @property
    def assess_quantity(self):
        return self._assess_quantity

    @assess_quantity.setter
    def assess_quantity(self, value):
        self._assess_quantity = value
    @property
    def assess_type(self):
        return self._assess_type

    @assess_type.setter
    def assess_type(self, value):
        self._assess_type = value
    @property
    def inspect_amount(self):
        return self._inspect_amount

    @inspect_amount.setter
    def inspect_amount(self, value):
        self._inspect_amount = value
    @property
    def inspect_quantity(self):
        return self._inspect_quantity

    @inspect_quantity.setter
    def inspect_quantity(self, value):
        self._inspect_quantity = value
    @property
    def unit_type(self):
        return self._unit_type

    @unit_type.setter
    def unit_type(self, value):
        self._unit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.assess_amount:
            if hasattr(self.assess_amount, 'to_alipay_dict'):
                params['assess_amount'] = self.assess_amount.to_alipay_dict()
            else:
                params['assess_amount'] = self.assess_amount
        if self.assess_max_amount:
            if hasattr(self.assess_max_amount, 'to_alipay_dict'):
                params['assess_max_amount'] = self.assess_max_amount.to_alipay_dict()
            else:
                params['assess_max_amount'] = self.assess_max_amount
        if self.assess_max_quantity:
            if hasattr(self.assess_max_quantity, 'to_alipay_dict'):
                params['assess_max_quantity'] = self.assess_max_quantity.to_alipay_dict()
            else:
                params['assess_max_quantity'] = self.assess_max_quantity
        if self.assess_min_amount:
            if hasattr(self.assess_min_amount, 'to_alipay_dict'):
                params['assess_min_amount'] = self.assess_min_amount.to_alipay_dict()
            else:
                params['assess_min_amount'] = self.assess_min_amount
        if self.assess_min_quantity:
            if hasattr(self.assess_min_quantity, 'to_alipay_dict'):
                params['assess_min_quantity'] = self.assess_min_quantity.to_alipay_dict()
            else:
                params['assess_min_quantity'] = self.assess_min_quantity
        if self.assess_quantity:
            if hasattr(self.assess_quantity, 'to_alipay_dict'):
                params['assess_quantity'] = self.assess_quantity.to_alipay_dict()
            else:
                params['assess_quantity'] = self.assess_quantity
        if self.assess_type:
            if hasattr(self.assess_type, 'to_alipay_dict'):
                params['assess_type'] = self.assess_type.to_alipay_dict()
            else:
                params['assess_type'] = self.assess_type
        if self.inspect_amount:
            if hasattr(self.inspect_amount, 'to_alipay_dict'):
                params['inspect_amount'] = self.inspect_amount.to_alipay_dict()
            else:
                params['inspect_amount'] = self.inspect_amount
        if self.inspect_quantity:
            if hasattr(self.inspect_quantity, 'to_alipay_dict'):
                params['inspect_quantity'] = self.inspect_quantity.to_alipay_dict()
            else:
                params['inspect_quantity'] = self.inspect_quantity
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
        o = MarketingProductInfo()
        if 'assess_amount' in d:
            o.assess_amount = d['assess_amount']
        if 'assess_max_amount' in d:
            o.assess_max_amount = d['assess_max_amount']
        if 'assess_max_quantity' in d:
            o.assess_max_quantity = d['assess_max_quantity']
        if 'assess_min_amount' in d:
            o.assess_min_amount = d['assess_min_amount']
        if 'assess_min_quantity' in d:
            o.assess_min_quantity = d['assess_min_quantity']
        if 'assess_quantity' in d:
            o.assess_quantity = d['assess_quantity']
        if 'assess_type' in d:
            o.assess_type = d['assess_type']
        if 'inspect_amount' in d:
            o.inspect_amount = d['inspect_amount']
        if 'inspect_quantity' in d:
            o.inspect_quantity = d['inspect_quantity']
        if 'unit_type' in d:
            o.unit_type = d['unit_type']
        return o



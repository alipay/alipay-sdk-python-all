#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttachGood(object):

    def __init__(self):
        self._attach_good_id = None
        self._attach_good_name = None
        self._attach_good_price = None
        self._quantity = None

    @property
    def attach_good_id(self):
        return self._attach_good_id

    @attach_good_id.setter
    def attach_good_id(self, value):
        self._attach_good_id = value
    @property
    def attach_good_name(self):
        return self._attach_good_name

    @attach_good_name.setter
    def attach_good_name(self, value):
        self._attach_good_name = value
    @property
    def attach_good_price(self):
        return self._attach_good_price

    @attach_good_price.setter
    def attach_good_price(self, value):
        self._attach_good_price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    def to_alipay_dict(self):
        params = dict()
        if self.attach_good_id:
            if hasattr(self.attach_good_id, 'to_alipay_dict'):
                params['attach_good_id'] = self.attach_good_id.to_alipay_dict()
            else:
                params['attach_good_id'] = self.attach_good_id
        if self.attach_good_name:
            if hasattr(self.attach_good_name, 'to_alipay_dict'):
                params['attach_good_name'] = self.attach_good_name.to_alipay_dict()
            else:
                params['attach_good_name'] = self.attach_good_name
        if self.attach_good_price:
            if hasattr(self.attach_good_price, 'to_alipay_dict'):
                params['attach_good_price'] = self.attach_good_price.to_alipay_dict()
            else:
                params['attach_good_price'] = self.attach_good_price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttachGood()
        if 'attach_good_id' in d:
            o.attach_good_id = d['attach_good_id']
        if 'attach_good_name' in d:
            o.attach_good_name = d['attach_good_name']
        if 'attach_good_price' in d:
            o.attach_good_price = d['attach_good_price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        return o



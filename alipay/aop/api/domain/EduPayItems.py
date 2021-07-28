#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduPayItems(object):

    def __init__(self):
        self._item_mandatory = None
        self._item_maximum = None
        self._item_name = None
        self._item_price = None
        self._item_serial_number = None

    @property
    def item_mandatory(self):
        return self._item_mandatory

    @item_mandatory.setter
    def item_mandatory(self, value):
        self._item_mandatory = value
    @property
    def item_maximum(self):
        return self._item_maximum

    @item_maximum.setter
    def item_maximum(self, value):
        self._item_maximum = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value
    @property
    def item_serial_number(self):
        return self._item_serial_number

    @item_serial_number.setter
    def item_serial_number(self, value):
        self._item_serial_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_mandatory:
            if hasattr(self.item_mandatory, 'to_alipay_dict'):
                params['item_mandatory'] = self.item_mandatory.to_alipay_dict()
            else:
                params['item_mandatory'] = self.item_mandatory
        if self.item_maximum:
            if hasattr(self.item_maximum, 'to_alipay_dict'):
                params['item_maximum'] = self.item_maximum.to_alipay_dict()
            else:
                params['item_maximum'] = self.item_maximum
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_price:
            if hasattr(self.item_price, 'to_alipay_dict'):
                params['item_price'] = self.item_price.to_alipay_dict()
            else:
                params['item_price'] = self.item_price
        if self.item_serial_number:
            if hasattr(self.item_serial_number, 'to_alipay_dict'):
                params['item_serial_number'] = self.item_serial_number.to_alipay_dict()
            else:
                params['item_serial_number'] = self.item_serial_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduPayItems()
        if 'item_mandatory' in d:
            o.item_mandatory = d['item_mandatory']
        if 'item_maximum' in d:
            o.item_maximum = d['item_maximum']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_price' in d:
            o.item_price = d['item_price']
        if 'item_serial_number' in d:
            o.item_serial_number = d['item_serial_number']
        return o


